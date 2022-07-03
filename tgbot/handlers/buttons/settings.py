from aiogram import types
from tgbot.data.data import _

from tgbot.keyboards.inline.language_keyboard import language_markup


async def settings(message: types.Message) -> None:
    await message.answer(
        text=_('Здравствуйте! Выберите необходимый язык'),
        reply_markup=language_markup()
    )
