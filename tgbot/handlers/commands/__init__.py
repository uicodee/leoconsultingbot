from aiogram import Dispatcher

from .start import user_start
from .register import register


def register_commands(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_message_handler(register, commands=["register"], state="*")
