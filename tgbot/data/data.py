from tgbot.middlewares import Language

i18n = Language(domain="messages", path="tgbot/locales", default="uz")
_ = i18n.gettext
__ = i18n.lazy_gettext

languages = {
    "ru": "๐ท๐บ ะ ัััะบะธะน",
    "uz": "๐บ๐ฟ O'zbek",
    "en": "๐บ๐ธ English"
}
