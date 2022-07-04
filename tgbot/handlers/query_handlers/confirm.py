from aiogram import types
from aiogram.dispatcher import FSMContext

from tgbot.keyboards.default.main_keyboard import main_markup
from tgbot.service.repo.application_repo import ApplicationRepo
from tgbot.service.repo.repository import SQLAlchemyRepos
from tgbot.data.data import _


async def confirm(query: types.CallbackQuery, state: FSMContext, repo: SQLAlchemyRepos):
    data = await state.get_data()
    await repo.get_repo(ApplicationRepo).new_application(
        name=data.get('name'),
        surname=data.get('surname'),
        age=int(data.get('age')),
        region=data.get('region'),
        phone_number=data.get('phone_number'),
    )
    await query.message.answer(
        text=_('Вы успешно зарегистрировались. Ждите звонка наших специалистов!'),
        reply_markup=main_markup()
    )
    await query.message.delete()
