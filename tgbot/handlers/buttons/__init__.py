from aiogram import Dispatcher
from tgbot.data.data import __
from .settings import settings
from .register import register


def register_buttons(dp: Dispatcher):
    dp.register_message_handler(settings, text=__('⚙️ Настройки'), state='*')
    dp.register_message_handler(register, text=__('👤 Ro\'yxatdan o\'tish'), state='*')
