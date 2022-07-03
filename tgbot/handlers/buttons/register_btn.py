from aiogram import types
from aiogram.dispatcher import FSMContext

from tgbot.data.data import _
from tgbot.states.states import RegisterForm


async def register_btn(message: types.Message, state: FSMContext) -> None:
    await state.reset_state(with_data=True)
    await message.answer(
        text=_('<b>Здравствуйте!</b>\n\n'
               'Как вас зовут?'),
        reply_markup=types.InlineKeyboardMarkup(
            row_width=1,
            inline_keyboard=[
                [types.InlineKeyboardButton(text=_('❌ Отмена'), callback_data='cancel')]
            ]
        )
    )
