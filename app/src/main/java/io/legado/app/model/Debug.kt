package io.legado.app.model

import android.annotation.SuppressLint
import android.util.Log
import io.legado.app.BuildConfig
import io.legado.app.constant.AppPattern
import io.legado.app.data.entities.*
import io.legado.app.help.book.isWebFile
import io.legado.app.help.coroutine.CompositeCoroutine
import io.legado.app.help.source.sortUrls
import io.legado.app.model.rss.Rss
import io.legado.app.model.webBook.WebBook
import io.legado.app.utils.HtmlFormatter
import io.legado.app.utils.isAbsUrl
import io.legado.app.utils.stackTraceStr
import kotlinx.coroutines.CoroutineScope
import java.text.SimpleDateFormat
import java.util.*

object Debug {
    var callback: Callback? = null
    private var debugSource: String? = null
    private val tasks: CompositeCoroutine = CompositeCoroutine()
    val debugMessageMap = HashMap<String, String>()
    private val debugTimeMap = HashMap<String, Long>()
    var isChecking: Boolean = false

    @SuppressLint("ConstantLocale")
    private val debugTimeFormat = SimpleDateFormat("[mm:ss.SSS]", Locale.getDefault())
    private var startTime: Long = System.currentTimeMillis()

    @Synchronized
    fun log(
        sourceUrl: String?,
        msg: String = "",
        print: Boolean = true,
        isHtml: Boolean = false,
        showTime: Boolean = true,
        state: Int = 1
    ) {
        if (BuildConfig.DEBUG) {
            Log.d("sourceDebug", msg)
        }
        //调试信息始终要执行
        callback?.let {
            if ((debugSource != sourceUrl || !print)) return
            var printMsg = msg
            if (isHtml) {
                printMsg = HtmlFormatter.format(msg)
            }
            if (showTime) {
                val time = debugTimeFormat.format(Date(System.currentTimeMillis() - startTime))
                printMsg = "$time $printMsg"
            }
            it.printLog(state, printMsg)
        }
        if (isChecking && sourceUrl != null && (msg).length < 30) {
            var printMsg = msg
            if (isHtml) {
                printMsg = HtmlFormatter.format(msg)
            }
            if (showTime && debugTimeMap[sourceUrl] != null) {
                val time =
                    debugTimeFormat.format(Date(System.currentTimeMillis() - debugTimeMap[sourceUrl]!!))
                printMsg = printMsg.replace(AppPattern.debugMessageSymbolRegex, "")

                debugMessageMap[sourceUrl] = "$time $printMsg"
            }
        }
    }

    @Synchronized
    fun log(msg: String?) {
        log(debugSource, msg ?: "", true)
    }

    fun cancelDebug(destroy: Boolean = false) {
        tasks.clear()

        if (destroy) {
            debugSource = null
            callback = null
        }
    }

    fun startChecking(source: BookSource) {
        isChecking = true
        debugTimeMap[source.bookSourceUrl] = System.currentTimeMillis()
        debugMessageMap[source.bookSourceUrl] = "${debugTimeFormat.format(Date(0))} bắt đầu xác minh"
    }

    fun finishChecking() {
        isChecking = false
    }

    fun getRespondTime(sourceUrl: String): Long {
        return debugTimeMap[sourceUrl] ?: CheckSource.timeout
    }

    fun updateFinalMessage(sourceUrl: String, state: String) {
        if (debugTimeMap[sourceUrl] != null && debugMessageMap[sourceUrl] != null) {
            val spendingTime = System.currentTimeMillis() - debugTimeMap[sourceUrl]!!
            debugTimeMap[sourceUrl] =
                if (state == "Xác thực thành công") spendingTime else CheckSource.timeout + spendingTime
            val printTime = debugTimeFormat.format(Date(spendingTime))
            debugMessageMap[sourceUrl] = "$printTime $state"
        }
    }

    suspend fun startDebug(scope: CoroutineScope, rssSource: RssSource) {
        cancelDebug()
        debugSource = rssSource.sourceUrl
        log(debugSource, "︾Bắt đầu phân tích cú pháp")
        val sort = rssSource.sortUrls().first()
        Rss.getArticles(scope, sort.first, sort.second, rssSource, 1)
            .onSuccess {
                if (it.first.isEmpty()) {
                    log(debugSource, "⇒Trang danh sách được phân tích cú pháp thành công và trống")
                    log(debugSource, "︽Phân tích hoàn thành", state = 1000)
                } else {
                    val ruleContent = rssSource.ruleContent
                    if (!rssSource.ruleArticles.isNullOrBlank() && rssSource.ruleDescription.isNullOrBlank()) {
                        log(debugSource, "︽Phân tích trang danh sách đã hoàn tất")
                        log(debugSource, showTime = false)
                        if (ruleContent.isNullOrEmpty()) {
                            log(debugSource, "⇒Quy tắc nội dung trống và toàn bộ trang web được lấy theo mặc định", state = 1000)
                        } else {
                            rssContentDebug(scope, it.first[0], ruleContent, rssSource)
                        }
                    } else {
                        log(debugSource, "⇒Có quy tắc mô tả, trang nội dung không được phân tích cú pháp")
                        log(debugSource, "︽Phân tích cú pháp hoàn tất", state = 1000)
                    }
                }
            }
            .onError {
                log(debugSource, it.stackTraceStr, state = -1)
            }
    }

    private fun rssContentDebug(
        scope: CoroutineScope,
        rssArticle: RssArticle,
        ruleContent: String,
        rssSource: RssSource
    ) {
        log(debugSource, "︾Bắt đầu phân tích trang nội dung")
        Rss.getContent(scope, rssArticle, ruleContent, rssSource)
            .onSuccess {
                log(debugSource, it)
                log(debugSource, "︽Đã hoàn tất phân tích trang nội dung", state = 1000)
            }
            .onError {
                log(debugSource, it.stackTraceStr, state = -1)
            }
    }

    fun startDebug(scope: CoroutineScope, bookSource: BookSource, key: String) {
        cancelDebug()
        debugSource = bookSource.bookSourceUrl
        startTime = System.currentTimeMillis()
        when {
            key.isAbsUrl() -> {
                val book = Book()
                book.origin = bookSource.bookSourceUrl
                book.bookUrl = key
                log(bookSource.bookSourceUrl, "⇒Bắt đầu truy cập trang chi tiết:$key")
                infoDebug(scope, bookSource, book)
            }

            key.contains("::") -> {
                val url = key.substringAfter("::")
                log(bookSource.bookSourceUrl, "⇒Bắt đầu truy cập trang khám phá:$url")
                exploreDebug(scope, bookSource, url)
            }

            key.startsWith("++") -> {
                val url = key.substring(2)
                val book = Book()
                book.origin = bookSource.bookSourceUrl
                book.tocUrl = url
                log(bookSource.bookSourceUrl, "⇒Bắt đầu truy cập trang danh mục:$url")
                tocDebug(scope, bookSource, book)
            }

            key.startsWith("--") -> {
                val url = key.substring(2)
                val book = Book()
                book.origin = bookSource.bookSourceUrl
                log(bookSource.bookSourceUrl, "⇒Bắt đầu truy cập trang văn bản:$url")
                val chapter = BookChapter()
                chapter.title = "gỡ lỗi"
                chapter.url = url
                contentDebug(scope, bookSource, book, chapter, null)
            }

            else -> {
                log(bookSource.bookSourceUrl, "⇒bắt đầu tìm kiếm từ khóa:$key")
                searchDebug(scope, bookSource, key)
            }
        }
    }

    private fun exploreDebug(scope: CoroutineScope, bookSource: BookSource, url: String) {
        log(debugSource, "︾Bắt đầu phân tích cú pháp trang khám phá")
        val explore = WebBook.exploreBook(scope, bookSource, url, 1)
            .onSuccess { exploreBooks ->
                if (exploreBooks.isNotEmpty()) {
                    log(debugSource, "︽Đã hoàn tất phân tích cú pháp trang khám phá")
                    log(debugSource, showTime = false)
                    infoDebug(scope, bookSource, exploreBooks[0].toBook())
                } else {
                    log(debugSource, "︽Sách không lấy được", state = -1)
                }
            }
            .onError {
                log(debugSource, it.stackTraceStr, state = -1)
            }
        tasks.add(explore)
    }

    private fun searchDebug(scope: CoroutineScope, bookSource: BookSource, key: String) {
        log(debugSource, "︾Bắt đầu phân tích trang tìm kiếm")
        val search = WebBook.searchBook(scope, bookSource, key, 1)
            .onSuccess { searchBooks ->
                if (searchBooks.isNotEmpty()) {
                    log(debugSource, "︽Đã hoàn tất phân tích cú pháp trang tìm kiếm")
                    log(debugSource, showTime = false)
                    infoDebug(scope, bookSource, searchBooks[0].toBook())
                } else {
                    log(debugSource, "︽Sách không lấy được", state = -1)
                }
            }
            .onError {
                log(debugSource, it.stackTraceStr, state = -1)
            }
        tasks.add(search)
    }

    private fun infoDebug(scope: CoroutineScope, bookSource: BookSource, book: Book) {
        if (book.tocUrl.isNotBlank()) {
            log(debugSource, "≡Đã lấy được link thư mục, bỏ qua trang chi tiết")
            log(debugSource, showTime = false)
            tocDebug(scope, bookSource, book)
            return
        }
        log(debugSource, "︾Bắt đầu phân tích trang chi tiết")
        val info = WebBook.getBookInfo(scope, bookSource, book)
            .onSuccess {
                log(debugSource, "︽Phân tích trang chi tiết đã hoàn thành")
                log(debugSource, showTime = false)
                if (!book.isWebFile) {
                    tocDebug(scope, bookSource, book)
                } else {
                    log(debugSource, "≡tệp lớp sách nguồn bỏ qua thư mục phân tích cú pháp", state = 1000)
                }
            }
            .onError {
                log(debugSource, it.stackTraceStr, state = -1)
            }
        tasks.add(info)
    }

    private fun tocDebug(scope: CoroutineScope, bookSource: BookSource, book: Book) {
        log(debugSource, "︾Bắt đầu phân tích cú pháp các trang danh mục")
        val chapterList = WebBook.getChapterList(scope, bookSource, book)
            .onSuccess { chapters ->
                log(debugSource, "︽Hoàn thành phân tích cú pháp trang danh mục")
                log(debugSource, showTime = false)
                val toc = chapters.filter { !(it.isVolume && it.url.startsWith(it.title)) }
                val nextChapterUrl = toc.getOrNull(1)?.url ?: toc.first().url
                contentDebug(scope, bookSource, book, toc.first(), nextChapterUrl)
            }
            .onError {
                log(debugSource, it.stackTraceStr, state = -1)
            }
        tasks.add(chapterList)
    }

    private fun contentDebug(
        scope: CoroutineScope,
        bookSource: BookSource,
        book: Book,
        bookChapter: BookChapter,
        nextChapterUrl: String?
    ) {
        log(debugSource, "︾Bắt đầu phân tích trang nội dung")
        val content = WebBook.getContent(
            scope = scope,
            bookSource = bookSource,
            book = book,
            bookChapter = bookChapter,
            nextChapterUrl = nextChapterUrl,
            needSave = false
        ).onSuccess {
            log(debugSource, "︽Đã hoàn tất phân tích cú pháp trang nội dung", state = 1000)
        }.onError {
            log(debugSource, it.stackTraceStr, state = -1)
        }
        tasks.add(content)
    }

    interface Callback {
        fun printLog(state: Int, msg: String)
    }
}