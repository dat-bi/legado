package io.legado.app

import androidx.test.ext.junit.runners.AndroidJUnit4
import com.google.gson.Gson
import io.legado.app.R
import io.legado.app.exception.NoStackTraceException
import io.legado.app.help.http.okHttpClient
import io.legado.app.help.update.GithubRelease
import io.legado.app.utils.fromJsonObject
import okhttp3.Request
import org.junit.Assert.assertTrue
import org.junit.Test
import org.junit.runner.RunWith
import splitties.init.appCtx

@RunWith(AndroidJUnit4::class)

class UpdateTest {

    private val lastReleaseUrl =
        "https://api.github.com/repos/gedoor/legado/releases/latest"

    private val lastBetaReleaseUrl =
        "https://api.github.com/repos/gedoor/legado/releases/tags/beta"

    @Test
    fun updateApp_beta() {
        val body = okHttpClient.newCall(Request.Builder().url(lastBetaReleaseUrl).build()).execute()
            .body!!.string()

        val releaseList = Gson().fromJsonObject<GithubRelease>(body)
            .getOrElse {
                throw NoStackTraceException(appCtx.getString(R.string.error_get_new_version) + " " + it.localizedMessage)
            }
            .gitReleaseToAppReleaseInfo()
            .sortedByDescending { it.createdAt }

        assertTrue(releaseList.size == 2)
        assertTrue(releaseList.all { it.downloadUrl.isNotBlank() })
        assertTrue(releaseList.all { it.versionName.isNotBlank() })
    }

    @Test
    fun updateApp() {
        val body = okHttpClient.newCall(Request.Builder().url(lastReleaseUrl).build()).execute()
            .body!!.string()

        val releaseList = Gson().fromJsonObject<GithubRelease>(body)
            .getOrElse {
                throw NoStackTraceException(appCtx.getString(R.string.error_get_new_version) + " " + it.localizedMessage)
            }
            .gitReleaseToAppReleaseInfo()
            .sortedByDescending { it.createdAt }

        assertTrue(releaseList.size == 1)
        assertTrue(releaseList.all { it.downloadUrl.isNotBlank() })
        assertTrue(releaseList.all { it.versionName.isNotBlank() })
    }

}