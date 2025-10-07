package io.legado.app.api.controller


import android.text.TextUtils
import io.legado.app.R
import io.legado.app.api.ReturnData
import io.legado.app.data.appDb
import io.legado.app.data.entities.BookSource
import io.legado.app.help.source.SourceHelp
import io.legado.app.utils.GSON
import io.legado.app.utils.fromJsonArray
import io.legado.app.utils.fromJsonObject
import splitties.init.appCtx

object BookSourceController {

    val sources: ReturnData
        get() {
            val bookSources = appDb.bookSourceDao.all
            val returnData = ReturnData()
            return if (bookSources.isEmpty()) {
                returnData.setErrorMsg(appCtx.getString(R.string.error_source_list_empty))
            } else returnData.setData(bookSources)
        }

    fun saveSource(postData: String?): ReturnData {
        val returnData = ReturnData()
        postData ?: return returnData.setErrorMsg(appCtx.getString(R.string.error_data_cannot_empty))
        val bookSource = GSON.fromJsonObject<BookSource>(postData).getOrNull()
        if (bookSource != null) {
            if (TextUtils.isEmpty(bookSource.bookSourceName) || TextUtils.isEmpty(bookSource.bookSourceUrl)) {
                returnData.setErrorMsg(appCtx.getString(R.string.error_source_name_url_empty))
            } else {
                appDb.bookSourceDao.insert(bookSource)
                returnData.setData("")
            }
        } else {
            returnData.setErrorMsg(appCtx.getString(R.string.error_convert_source_failed))
        }
        return returnData
    }

    fun saveSources(postData: String?): ReturnData {
        postData ?: return ReturnData().setErrorMsg(appCtx.getString(R.string.error_data_empty))
        val okSources = arrayListOf<BookSource>()
        val bookSources = GSON.fromJsonArray<BookSource>(postData).getOrNull()
        if (bookSources.isNullOrEmpty()) {
            return ReturnData().setErrorMsg(appCtx.getString(R.string.error_convert_source_failed))
        }
        bookSources.forEach { bookSource ->
            if (bookSource.bookSourceName.isNotBlank()
                && bookSource.bookSourceUrl.isNotBlank()
            ) {
                appDb.bookSourceDao.insert(bookSource)
                okSources.add(bookSource)
            }
        }
        return ReturnData().setData(okSources)
    }

    fun getSource(parameters: Map<String, List<String>>): ReturnData {
        val url = parameters["url"]?.firstOrNull()
        val returnData = ReturnData()
        if (url.isNullOrEmpty()) {
            return returnData.setErrorMsg(appCtx.getString(R.string.error_url_param_empty))
        }
        val bookSource = appDb.bookSourceDao.getBookSource(url)
            ?: return returnData.setErrorMsg(appCtx.getString(R.string.error_book_source_not_found_simple))
        return returnData.setData(bookSource)
    }

    fun deleteSources(postData: String?): ReturnData {
        kotlin.runCatching {
            GSON.fromJsonArray<BookSource>(postData).getOrThrow().let {
                SourceHelp.deleteBookSources(it)
            }
        }.onFailure {
            return ReturnData().setErrorMsg(it.localizedMessage ?: appCtx.getString(R.string.error_format_invalid))
        }
        return ReturnData().setData(appCtx.getString(R.string.action_done))
    }
}
