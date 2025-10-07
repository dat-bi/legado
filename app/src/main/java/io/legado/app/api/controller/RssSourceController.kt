package io.legado.app.api.controller


import android.text.TextUtils
import io.legado.app.R
import io.legado.app.api.ReturnData
import io.legado.app.data.appDb
import io.legado.app.data.entities.RssSource
import io.legado.app.help.source.SourceHelp
import io.legado.app.utils.GSON
import io.legado.app.utils.fromJsonArray
import io.legado.app.utils.fromJsonObject
import splitties.init.appCtx

object RssSourceController {

    val sources: ReturnData
        get() {
            val source = appDb.rssSourceDao.all
            val returnData = ReturnData()
            return if (source.isEmpty()) {
                returnData.setErrorMsg(appCtx.getString(R.string.error_source_list_empty))
            } else returnData.setData(source)
        }

    fun saveSource(postData: String?): ReturnData {
        val returnData = ReturnData()
        postData ?: return returnData.setErrorMsg(appCtx.getString(R.string.error_data_cannot_empty))
        GSON.fromJsonObject<RssSource>(postData).onFailure {
            returnData.setErrorMsg(appCtx.getString(R.string.error_convert_source_failed) + "${it.localizedMessage}")
        }.onSuccess { source ->
            if (TextUtils.isEmpty(source.sourceName) || TextUtils.isEmpty(source.sourceUrl)) {
                returnData.setErrorMsg(appCtx.getString(R.string.error_source_name_url_empty))
            } else {
                appDb.rssSourceDao.insert(source)
                returnData.setData("")
            }
        }
        return returnData
    }

    fun saveSources(postData: String?): ReturnData {
        postData ?: return ReturnData().setErrorMsg(appCtx.getString(R.string.error_data_cannot_empty))
        val okSources = arrayListOf<RssSource>()
        val source = GSON.fromJsonArray<RssSource>(postData).getOrNull()
        if (source.isNullOrEmpty()) {
            return ReturnData().setErrorMsg(appCtx.getString(R.string.error_convert_source_failed))
        }
        for (rssSource in source) {
            if (rssSource.sourceName.isBlank() || rssSource.sourceUrl.isBlank()) {
                continue
            }
            appDb.rssSourceDao.insert(rssSource)
            okSources.add(rssSource)
        }
        return ReturnData().setData(okSources)
    }

    fun getSource(parameters: Map<String, List<String>>): ReturnData {
        val url = parameters["url"]?.firstOrNull()
        val returnData = ReturnData()
        if (url.isNullOrEmpty()) {
            return returnData.setErrorMsg(appCtx.getString(R.string.error_url_param_empty))
        }
        val source = appDb.rssSourceDao.getByKey(url)
            ?: return returnData.setErrorMsg(appCtx.getString(R.string.error_source_not_found))
        return returnData.setData(source)
    }

    fun deleteSources(postData: String?): ReturnData {
        postData ?: return ReturnData().setErrorMsg(appCtx.getString(R.string.error_no_data_passed))
        GSON.fromJsonArray<RssSource>(postData).onFailure {
            return ReturnData().setErrorMsg(appCtx.getString(R.string.error_format_invalid))
        }.onSuccess {
            SourceHelp.deleteRssSources(it)
        }
        return ReturnData().setData(appCtx.getString(R.string.action_done))
    }
}
