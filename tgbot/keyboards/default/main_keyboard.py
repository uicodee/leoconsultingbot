from aiogram import types
from tgbot.data.data import _


def main_markup(**kwargs) -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text=_('👤 Отправить заявку', locale=kwargs.get('locale'))),
        types.KeyboardButton(text=_('⚙️ Настройки', locale=kwargs.get('locale'))),
    )
    return keyboard
