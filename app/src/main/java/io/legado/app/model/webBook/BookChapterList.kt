package io.legado.app.model.webBook

import android.text.TextUtils
import com.script.SimpleBindings
import com.script.rhino.RhinoScriptEngine
import io.legado.app.R
import io.legado.app.data.entities.Book
import io.legado.app.data.entities.BookChapter
import io.legado.app.data.entities.BookSource
import io.legado.app.data.entities.rule.TocRule
import io.legado.app.exception.NoStackTraceException
import io.legado.app.exception.TocEmptyException
import io.legado.app.help.book.ContentProcessor
import io.legado.app.model.Debug
import io.legado.app.model.analyzeRule.AnalyzeRule
import io.legado.app.model.analyzeRule.AnalyzeUrl
import io.legado.app.utils.isTrue
import kotlinx.coroutines.Dispatchers.IO
import kotlinx.coroutines.async
import kotlinx.coroutines.ensureActive
import kotlinx.coroutines.withContext
import splitties.init.appCtx
import kotlin.coroutines.coroutineContext

/**
*lấy thư mục
*/
object BookChapterList {

    suspend fun analyzeChapterList(
        bookSource: BookSource,
        book: Book,
        baseUrl: String,
        redirectUrl: String,
        body: String?
    ): List<BookChapter> {
        body ?: throw NoStackTraceException(
            appCtx.getString(R.string.error_get_web_content, baseUrl)
        )
        val chapterList = ArrayList<BookChapter>()
        Debug.log(bookSource.bookSourceUrl, "≡Thu hoạch thành công:${baseUrl}")
        Debug.log(bookSource.bookSourceUrl, body, state = 30)
        val tocRule = bookSource.getTocRule()
        val nextUrlList = arrayListOf(redirectUrl)
        var reverse = false
        var listRule = tocRule.chapterList ?: ""
        if (listRule.startsWith("-")) {
            reverse = true
            listRule = listRule.substring(1)
        }
        if (listRule.startsWith("+")) {
            listRule = listRule.substring(1)
        }
        var chapterData =
            analyzeChapterList(
                book, baseUrl, redirectUrl, body,
                tocRule, listRule, bookSource, log = true
            )
        chapterList.addAll(chapterData.first)
        when (chapterData.second.size) {
            0 -> Unit
            1 -> {
                var nextUrl = chapterData.second[0]
                while (nextUrl.isNotEmpty() && !nextUrlList.contains(nextUrl)) {
                    nextUrlList.add(nextUrl)
                    val res = AnalyzeUrl(
                        mUrl = nextUrl,
                        source = bookSource,
                        ruleData = book,
                        headerMapF = bookSource.getHeaderMap()
                    ).getStrResponseAwait() //控制并发访问
                    res.body?.let { nextBody ->
                        chapterData = analyzeChapterList(
                            book, nextUrl, nextUrl,
                            nextBody, tocRule, listRule, bookSource
                        )
                        nextUrl = chapterData.second.firstOrNull() ?: ""
                        chapterList.addAll(chapterData.first)
                    }
                }
                Debug.log(bookSource.bookSourceUrl, "◇Tổng số trang của danh mục:${nextUrlList.size}")
            }

            else -> {
                Debug.log(
                    bookSource.bookSourceUrl,
                    "◇Đồng phát phân tích mục lục, tổng số trang:${chapterData.second.size}"
                )
                withContext(IO) {
                    val asyncArray = Array(chapterData.second.size) {
                        async(IO) {
                            val urlStr = chapterData.second[it]
                            val res = AnalyzeUrl(
                                mUrl = urlStr,
                                source = bookSource,
                                ruleData = book,
                                headerMapF = bookSource.getHeaderMap()
                            ).getStrResponseAwait() //控制并发访问
                            analyzeChapterList(
                                book, urlStr, res.url,
                                res.body!!, tocRule, listRule, bookSource, false
                            ).first
                        }
                    }
                    asyncArray.forEach { coroutine ->
                        chapterList.addAll(coroutine.await())
                    }
                }
            }
        }
        if (chapterList.isEmpty()) {
            throw TocEmptyException(appCtx.getString(R.string.chapter_list_empty))
        }
        //去重
        if (!reverse) {
            chapterList.reverse()
        }
        coroutineContext.ensureActive()
        val lh = LinkedHashSet(chapterList)
        val list = ArrayList(lh)
        if (!book.getReverseToc()) {
            list.reverse()
        }
        Debug.log(book.origin, "◇Tổng số mục lục:${list.size}")
        coroutineContext.ensureActive()
        val formatJs = tocRule.formatJs
        val bindings = SimpleBindings()
        bindings["gInt"] = 0
        list.forEachIndexed { index, bookChapter ->
            bookChapter.index = index
            if (!formatJs.isNullOrBlank()) {
                bindings["index"] = index + 1
                bindings["chapter"] = bookChapter
                bindings["title"] = bookChapter.title
                RhinoScriptEngine.runCatching {
                    eval(formatJs, bindings)?.toString()?.let {
                        bookChapter.title = it
                    }
                }.onFailure {
                    Debug.log(book.origin, "Format tiêu đề phạm sai lầm, ${it.localizedMessage}")
                }
            }
        }
        val replaceRules = ContentProcessor.get(book.name, book.origin).getTitleReplaceRules()
        book.latestChapterTitle = list.last().getDisplayTitle(replaceRules)
        book.durChapterTitle = list.getOrElse(book.durChapterIndex) { list.last() }
            .getDisplayTitle(replaceRules)
        if (book.totalChapterNum < list.size) {
            book.lastCheckCount = list.size - book.totalChapterNum
            book.latestChapterTime = System.currentTimeMillis()
        }
        book.lastCheckTime = System.currentTimeMillis()
        book.totalChapterNum = list.size
        coroutineContext.ensureActive()
        return list
    }

    private suspend fun analyzeChapterList(
        book: Book,
        baseUrl: String,
        redirectUrl: String,
        body: String,
        tocRule: TocRule,
        listRule: String,
        bookSource: BookSource,
        getNextUrl: Boolean = true,
        log: Boolean = false
    ): Pair<List<BookChapter>, List<String>> {
        val analyzeRule = AnalyzeRule(book, bookSource)
        analyzeRule.setContent(body).setBaseUrl(baseUrl)
        analyzeRule.setRedirectUrl(redirectUrl)
        //获取目录列表
        val chapterList = arrayListOf<BookChapter>()
        Debug.log(bookSource.bookSourceUrl, "┌Thu hoạch mục lục danh sách", log)
        val elements = analyzeRule.getElements(listRule)
        Debug.log(bookSource.bookSourceUrl, "└Danh sách lớn nhỏ:${elements.size}", log)
        //获取下一页链接
        val nextUrlList = arrayListOf<String>()
        val nextTocRule = tocRule.nextTocUrl
        if (getNextUrl && !nextTocRule.isNullOrEmpty()) {
            Debug.log(bookSource.bookSourceUrl, "┌Thu hoạch mục lục trang kế tiếp danh sách", log)
            analyzeRule.getStringList(nextTocRule, isUrl = true)?.let {
                for (item in it) {
                    if (item != redirectUrl) {
                        nextUrlList.add(item)
                    }
                }
            }
            Debug.log(
                bookSource.bookSourceUrl,
                "└" + TextUtils.join("，\n", nextUrlList),
                log
            )
        }
        coroutineContext.ensureActive()
        if (elements.isNotEmpty()) {
            Debug.log(bookSource.bookSourceUrl, "┌Phân tích mục lục danh sách", log)
            val nameRule = analyzeRule.splitSourceRule(tocRule.chapterName)
            val urlRule = analyzeRule.splitSourceRule(tocRule.chapterUrl)
            val vipRule = analyzeRule.splitSourceRule(tocRule.isVip)
            val payRule = analyzeRule.splitSourceRule(tocRule.isPay)
            val upTimeRule = analyzeRule.splitSourceRule(tocRule.updateTime)
            val isVolumeRule = analyzeRule.splitSourceRule(tocRule.isVolume)
            elements.forEachIndexed { index, item ->
                coroutineContext.ensureActive()
                analyzeRule.setContent(item)
                val bookChapter = BookChapter(bookUrl = book.bookUrl, baseUrl = redirectUrl)
                analyzeRule.chapter = bookChapter
                bookChapter.title = analyzeRule.getString(nameRule)
                bookChapter.url = analyzeRule.getString(urlRule)
                bookChapter.tag = analyzeRule.getString(upTimeRule)
                val isVolume = analyzeRule.getString(isVolumeRule)
                bookChapter.isVolume = false
                if (isVolume.isTrue()) {
                    bookChapter.isVolume = true
                }
                if (bookChapter.url.isEmpty()) {
                    if (bookChapter.isVolume) {
                        bookChapter.url = bookChapter.title + index
                        Debug.log(
                            bookSource.bookSourceUrl,
                            "⇒Cấp 1 mục lục ${index} Không thu hoạch đến url, sử dụng tiêu đề thay thế"
                        )
                    } else {
                        bookChapter.url = baseUrl
                        Debug.log(
                            bookSource.bookSourceUrl,
                            "⇒Mục lục ${index} Không thu hoạch đến url, sử dụng baseUrl thay thế"
                        )
                    }
                }
                if (bookChapter.title.isNotEmpty()) {
                    val isVip = analyzeRule.getString(vipRule)
                    val isPay = analyzeRule.getString(payRule)
                    if (isVip.isTrue()) {
                        bookChapter.isVip = true
                    }
                    if (isPay.isTrue()) {
                        bookChapter.isPay = true
                    }
                    chapterList.add(bookChapter)
                }
            }
            Debug.log(bookSource.bookSourceUrl, "└Mục lục danh sách phân tích hoàn thành", log)
            if (chapterList.isEmpty()) {
                Debug.log(bookSource.bookSourceUrl, "◇Chương tiết danh sách vì khoảng không", log)
            } else {
                Debug.log(bookSource.bookSourceUrl, "≡Thông tin chương", log)
                Debug.log(bookSource.bookSourceUrl, "◇Tên chương:${chapterList[0].title}", log)
                Debug.log(bookSource.bookSourceUrl, "◇URL chương:${chapterList[0].url}", log)
                Debug.log(bookSource.bookSourceUrl, "◇Thông tin chương:${chapterList[0].tag}", log)
                Debug.log(bookSource.bookSourceUrl, "◇là VIP:${chapterList[0].isVip}", log)
                Debug.log(bookSource.bookSourceUrl, "◇Phải chăng mua sắm:${chapterList[0].isPay}", log)
            }
        }
        return Pair(chapterList, nextUrlList)
    }

}