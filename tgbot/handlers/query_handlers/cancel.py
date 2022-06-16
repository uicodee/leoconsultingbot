from aiogram import types
from aiogram.dispatcher import FSMContext


async def cancel(query: types.CallbackQuery, state: FSMContext):
    await query.answer()
    await query.message.delete()
    await state.reset_state(with_data=True)
