from aiogram import Dispatcher
from tgbot.data.data import __
from .settings import settings
from .register_btn import register_btn


def register_buttons(dp: Dispatcher):
    dp.register_message_handler(settings, text=__('⚙️ Настройки'), state='*')
    dp.register_message_handler(register_btn, text=__('👤 Отправить заявку'), state='*')
