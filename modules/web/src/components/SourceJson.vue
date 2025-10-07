<template>
  <el-input
    id="source-json"
    v-model="sourceString"
    type="textarea"
    :placeholder="$t('sourceJson.placeholder')"
    :rows="30"
    @change="update"
    style="margin-bottom: 4px"
  ></el-input>
</template>
<script setup lang="ts">
import { useSourceStore } from '@/store'
import { useI18n } from 'vue-i18n'

const { t } = useI18n()
const store = useSourceStore()
const sourceString = ref('')
const update = async (string: string) => {
  try {
    store.changeEditTabSource(JSON.parse(string))
  } catch {
    ElMessage({
      message: t('sourceJson.formatError'),
      type: 'error',
    })
  }
}

watchEffect(async () => {
  const source = store.editTabSource
  if (Object.keys(source).length > 0) {
    sourceString.value = JSON.stringify(source, null, 4)
  } else {
    sourceString.value = ''
  }
})
</script>
<style lang="scss" scoped>
:deep(.el-input) {
  width: 100%;
}
:deep(#source-json) {
  height: calc(100vh - 50px);
}
</style>
