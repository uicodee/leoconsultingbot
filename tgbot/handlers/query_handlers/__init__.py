from aiogram import Dispatcher

from tgbot.callback_data.callback_datas import cb_language
from .cancel import cancel

from .language_handler import language_handler
from .confirm import confirm


def register_query_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(cancel, text='cancel', state="*")
    dp.register_callback_query_handler(language_handler, cb_language.filter(), state="*")
    dp.register_callback_query_handler(confirm, text='confirm', state="*")
