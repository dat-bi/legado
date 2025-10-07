import { createApp } from 'vue'
import App from './App.vue'
import router from '@/router'
import store from '@/store'
import i18n from '@/i18n'
import 'element-plus/theme-chalk/dark/css-vars.css'

createApp(App).use(store).use(router).use(i18n).mount('#app')
// 书架 同步Element PLUS 夜间模式
watch(
  () => useBookStore().isNight,
  isNight => {
    if (isNight) {
      document.documentElement.classList.add('dark')
    } else {
      document.documentElement.classList.remove('dark')
    }
  },
)

window.addEventListener('vite:preloadError', event => {
  event.preventDefault()
})
