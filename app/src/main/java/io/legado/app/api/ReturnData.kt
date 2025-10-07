package io.legado.app.api

import androidx.annotation.Keep
import io.legado.app.R
import io.legado.app.utils.appCtx

@Keep
class ReturnData {

    var isSuccess: Boolean = false
        private set

    var errorMsg: String = appCtx.getString(R.string.error_unknown)
        private set

    var data: Any? = null
        private set

    fun setErrorMsg(errorMsg: String): ReturnData {
        this.isSuccess = false
        this.errorMsg = errorMsg
        return this
    }

    fun setData(data: Any): ReturnData {
        this.isSuccess = true
        this.errorMsg = ""
        this.data = data
        return this
    }
}
