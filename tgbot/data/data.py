from tgbot.middlewares import Language

i18n = Language(domain="messages", path="locales", default="uz")
_ = i18n.gettext
__ = i18n.lazy_gettext

languages = {
    "ru": "🇷🇺 Русский",
    "uz": "🇺🇿 O'zbek",
    "en": "🇺🇸 English"
}
