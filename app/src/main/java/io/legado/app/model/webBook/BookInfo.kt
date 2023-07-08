package io.legado.app.model.webBook

import android.text.TextUtils
import io.legado.app.R
import io.legado.app.data.entities.Book
import io.legado.app.data.entities.BookSource
import io.legado.app.exception.NoStackTraceException
import io.legado.app.help.book.BookHelp
import io.legado.app.help.book.isWebFile
import io.legado.app.model.Debug
import io.legado.app.model.analyzeRule.AnalyzeRule
import io.legado.app.utils.DebugLog
import io.legado.app.utils.HtmlFormatter
import io.legado.app.utils.NetworkUtils
import io.legado.app.utils.StringUtils.wordCountFormat
import kotlinx.coroutines.ensureActive
import splitties.init.appCtx
import kotlin.coroutines.coroutineContext


/**
 * 获取详情
 */
object BookInfo {

    @Throws(Exception::class)
    suspend fun analyzeBookInfo(
        bookSource: BookSource,
        book: Book,
        baseUrl: String,
        redirectUrl: String,
        body: String?,
        canReName: Boolean,
    ) {
        body ?: throw NoStackTraceException(
            appCtx.getString(R.string.error_get_web_content, baseUrl)
        )
        Debug.log(bookSource.bookSourceUrl, "≡Thu hoạch thành công:${baseUrl}")
        Debug.log(bookSource.bookSourceUrl, body, state = 20)
        val analyzeRule = AnalyzeRule(book, bookSource)
        analyzeRule.setContent(body).setBaseUrl(baseUrl)
        analyzeRule.setRedirectUrl(redirectUrl)
        analyzeBookInfo(book, body, analyzeRule, bookSource, baseUrl, redirectUrl, canReName)
    }

    suspend fun analyzeBookInfo(
        book: Book,
        body: String,
        analyzeRule: AnalyzeRule,
        bookSource: BookSource,
        baseUrl: String,
        redirectUrl: String,
        canReName: Boolean,
    ) {
        val infoRule = bookSource.getBookInfoRule()
        infoRule.init?.let {
            if (it.isNotBlank()) {
                coroutineContext.ensureActive()
                Debug.log(bookSource.bookSourceUrl, "≡Thực hiện các quy tắc khởi tạo trang chi tiết")
                analyzeRule.setContent(analyzeRule.getElement(it))
            }
        }
        val mCanReName = canReName && !infoRule.canReName.isNullOrBlank()
        coroutineContext.ensureActive()
        Debug.log(bookSource.bookSourceUrl, "┌Thu hoạch tiêu đề")
        BookHelp.formatBookName(analyzeRule.getString(infoRule.name)).let {
            if (it.isNotEmpty() && (mCanReName || book.name.isEmpty())) {
                book.name = it
            }
            Debug.log(bookSource.bookSourceUrl, "└${it}")
        }
        coroutineContext.ensureActive()
        Debug.log(bookSource.bookSourceUrl, "┌Thu hoạch tác giả")
        BookHelp.formatBookAuthor(analyzeRule.getString(infoRule.author)).let {
            if (it.isNotEmpty() && (mCanReName || book.author.isEmpty())) {
                book.author = it
            }
            Debug.log(bookSource.bookSourceUrl, "└${it}")
        }
        coroutineContext.ensureActive()
        Debug.log(bookSource.bookSourceUrl, "┌Thu hoạch danh mục")
        try {
            analyzeRule.getStringList(infoRule.kind)
                ?.joinToString(",")
                ?.let {
                    if (it.isNotEmpty()) book.kind = it
                    Debug.log(bookSource.bookSourceUrl, "└${it}")
                } ?: Debug.log(bookSource.bookSourceUrl, "└")
        } catch (e: Exception) {
            Debug.log(bookSource.bookSourceUrl, "└${e.localizedMessage}")
            DebugLog.e("Lỗi nhận danh mục", e)
        }
        coroutineContext.ensureActive()
        Debug.log(bookSource.bookSourceUrl, "┌đếm từ(wordCount)")
        try {
            wordCountFormat(analyzeRule.getString(infoRule.wordCount)).let {
                if (it.isNotEmpty()) book.wordCount = it
                Debug.log(bookSource.bookSourceUrl, "└${it}")
            }
        } catch (e: Exception) {
            Debug.log(bookSource.bookSourceUrl, "└${e.localizedMessage}")
            DebugLog.e("Bắt lỗi đếm từ(wordCount)", e)
        }
        coroutineContext.ensureActive()
        Debug.log(bookSource.bookSourceUrl, "┌Nhận chương mới nhất")
        try {
            analyzeRule.getString(infoRule.lastChapter).let {
                if (it.isNotEmpty()) book.latestChapterTitle = it
                Debug.log(bookSource.bookSourceUrl, "└${it}")
            }
        } catch (e: Exception) {
            Debug.log(bookSource.bookSourceUrl, "└${e.localizedMessage}")
            DebugLog.e("Lỗi nhận chương mới nhất", e)
        }
        coroutineContext.ensureActive()
        Debug.log(bookSource.bookSourceUrl, "┌Thu hoạch giới thiệu vắn tắt")
        try {
            HtmlFormatter.format(analyzeRule.getString(infoRule.intro)).let {
                if (it.isNotEmpty()) book.intro = it
                Debug.log(bookSource.bookSourceUrl, "└${it}")
            }
        } catch (e: Exception) {
            Debug.log(bookSource.bookSourceUrl, "└${e.localizedMessage}")
            DebugLog.e("Lỗi nhận giới thiệu vắn tắt", e)
        }
        coroutineContext.ensureActive()
        Debug.log(bookSource.bookSourceUrl, "┌Lấy link cover(bìa)")
        try {
            analyzeRule.getString(infoRule.coverUrl).let {
                if (it.isNotEmpty()) {
                    book.coverUrl =
                        NetworkUtils.getAbsoluteURL(redirectUrl, it)
                }
                Debug.log(bookSource.bookSourceUrl, "└${it}")
            }
        } catch (e: Exception) {
            Debug.log(bookSource.bookSourceUrl, "└${e.localizedMessage}")
            DebugLog.e("Lỗi nhận cover", e)
        }
        if (!book.isWebFile) {
            coroutineContext.ensureActive()
            Debug.log(bookSource.bookSourceUrl, "┌Thu hoạch mục lục kết nối")
            book.tocUrl = analyzeRule.getString(infoRule.tocUrl, isUrl = true)
            if (book.tocUrl.isEmpty()) book.tocUrl = baseUrl
            if (book.tocUrl == baseUrl) {
                book.tocHtml = body
            }
            Debug.log(bookSource.bookSourceUrl, "└${book.tocUrl}")
        } else {
            coroutineContext.ensureActive()
            Debug.log(bookSource.bookSourceUrl, "┌Lấy link tải file")
            book.downloadUrls = analyzeRule.getStringList(infoRule.downloadUrls, isUrl = true)
            if (book.downloadUrls.isNullOrEmpty()) {
                Debug.log(bookSource.bookSourceUrl, "└")
                throw NoStackTraceException("liên kết tải xuống trống")
            } else {
                Debug.log(
                    bookSource.bookSourceUrl,
                    "└" + TextUtils.join("，\n", book.downloadUrls!!)
                )
            }
        }
    }

}