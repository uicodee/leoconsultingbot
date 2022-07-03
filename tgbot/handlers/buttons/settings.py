from aiogram import types
from aiogram.dispatcher import FSMContext

from tgbot.data.data import _

from tgbot.keyboards.inline.language_keyboard import language_markup


async def settings(message: types.Message, state: FSMContext) -> None:
    await state.reset_state(with_data=True)
    await message.answer(
        text=_('Здравствуйте! Выберите необходимый язык'),
        reply_markup=language_markup()
    )
