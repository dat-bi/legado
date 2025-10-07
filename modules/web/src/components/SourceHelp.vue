<script setup lang="ts">
import { Link } from '@element-plus/icons-vue'
import { useI18n } from 'vue-i18n'

const { t } = useI18n()
</script>
<template>
  <el-link :icon="Link" href="/help/#appHelp" target="_blank"
    >{{ t('help.appHelp') }}</el-link
  ><br />
  <el-link :icon="Link" href="/help/#ruleHelp" target="_blank"
    >{{ t('help.ruleHelp') }}</el-link
  ><br />
  <el-link :icon="Link" href="/help/#jsHelp" target="_blank"
    >{{ t('help.jsHelp') }}</el-link
  ><br />
  <el-link :icon="Link" href="/help/#xpathHelp" target="_blank"
    >{{ t('help.xpathHelp') }}</el-link
  ><br />
  <el-link :icon="Link" href="/help/#regexHelp" target="_blank"
    >{{ t('help.regexHelp') }}</el-link
  ><br />
  <el-link :icon="Link" href="/help/#txtTocRuleHelp" target="_blank"
    >{{ t('help.txtTocRuleHelp') }}</el-link
  ><br />
  <el-link :icon="Link" href="/help/#debugHelp" target="_blank"
    >{{ t('help.debugHelp') }}</el-link
  ><br />
  <el-link :icon="Link" href="/help/#httpTTSHelp" target="_blank"
    >{{ t('help.httpTTSHelp') }}</el-link
  ><br />
  <el-link :icon="Link" href="/help/#webDavBookHelp" target="_blank">
    {{ t('help.webDavBookHelp') }}</el-link
  ><br />
  <el-link :icon="Link" href="/help/#webDavHelp" target="_blank">
    {{ t('help.webDavHelp') }}</el-link
  ><br />
  <el-link :icon="Link" href="https://regexr-cn.com/" target="_blank"
    >{{ t('help.regexOnlineValidator') }}</el-link
  ><br />
  <div style="margin-top: 20px">
    <span
      ><el-text
        ><code>^$()[]{}.?+*|</code> {{ t('help.javaRegexSpecialChars') }}</el-text
      ></span
    ><br />
    <span
      ><el-text><code>(?s)</code> {{ t('help.regexCrossLine') }}</el-text></span
    ><br />
    <span
      ><el-text><code>(?m)</code> {{ t('help.regexLineByLine') }}</el-text></span
    ><br />
    <span
      ><el-text><code>(?i)</code> {{ t('help.regexIgnoreCase') }}</el-text></span
    ><br />
  </div>
</template>

<style lang="scss" scoped>
.el-link {
  padding: 4px;
}
.el-text {
  padding-top: 20px;
}
</style>
