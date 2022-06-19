from aiogram import types
from aiogram.dispatcher import FSMContext

from tgbot.service.repo.application_repo import ApplicationRepo
from tgbot.service.repo.repository import SQLAlchemyRepos
from tgbot.data.data import _


async def confirm(query: types.CallbackQuery, state: FSMContext, repo: SQLAlchemyRepos):
    data = await state.get_data()
    await repo.get_repo(ApplicationRepo).new_application(
        name=data.get('name'),
        surname=data.get('surname'),
        age=int(data.get('age')),
        email=data.get('email'),
        region=data.get('region'),
        phone_number=data.get('phone_number'),
    )
    await query.answer(text=_('🥳 Ваши данные успешно сохранены и переданы на обработку!'), show_alert=True)
    await query.message.delete()
