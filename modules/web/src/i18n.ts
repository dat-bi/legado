import { createI18n } from 'vue-i18n'

import en from '@/locales/en.json'
import zh from '@/locales/zh.json'
import vi from '@/locales/vi.json'

export type Locale = 'en' | 'zh' | 'vi'

function getInitialLocale(): Locale {
    const saved = localStorage.getItem('locale') as Locale | null
    if (saved === 'en' || saved === 'zh' || saved === 'vi') return saved
    const lang = navigator.language.toLowerCase()
    if (lang.startsWith('zh')) return 'zh'
    if (lang.startsWith('vi')) return 'vi'
    return 'en'
}

export const i18n = createI18n({
    legacy: false,
    globalInjection: true,
    locale: getInitialLocale(),
    fallbackLocale: 'en',
    messages: { en, zh, vi },
})

export function setLocale(locale: Locale) {
    i18n.global.locale.value = locale
    localStorage.setItem('locale', locale)
}

export default i18n


