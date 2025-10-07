package io.legado.app

import androidx.test.ext.junit.runners.AndroidJUnit4
import io.legado.app.R
import io.legado.app.help.config.AppConfig
import io.legado.app.model.analyzeRule.AnalyzeUrl
import kotlinx.coroutines.runBlocking
import org.junit.Test
import org.junit.runner.RunWith
import splitties.init.appCtx

@RunWith(AndroidJUnit4::class)

class HttpTtsTest {

    @Test
    fun test() {
        val url = """
            http://tsn.baidu.com/text2audio,{
                "method": "POST",
                "body": "tex={{java.encodeURI(java.encodeURI(speakText))}}&spd={{(speakSpeed + 5) / 10 + 4}}&per=4114&cuid=baidu_speech_demo&idx=1&cod=2&lan=zh&ctp=1&pdt=220&vol=5&aue=6&pit=5&_res_tag_=audio"
            }
        """.trimIndent()
        val analyzeUrl =
            AnalyzeUrl(url, speakText = appCtx.getString(R.string.test_speak_text), speakSpeed = AppConfig.speechRatePlay + 5)
        runBlocking {
            val response = analyzeUrl.getResponseAwait()
            response.headers
        }
    }

}