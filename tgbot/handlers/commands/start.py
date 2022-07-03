from aiogram import types

from tgbot.data.data import _
from tgbot.keyboards.default.main_keyboard import main_markup
from tgbot.keyboards.inline.language_keyboard import language_markup
from tgbot.service.repo.repository import SQLAlchemyRepos
from tgbot.service.repo.user_repo import UserRepo
from tgbot.states.states import RegisterForm


async def user_start(message: types.Message, repo: SQLAlchemyRepos):
    user = repo.get_repo(UserRepo)
    if await user.get_user(user_id=message.from_user.id) is None:
        await message.answer(
            text=_('Здравствуйте! Выберите необходимый язык'),
            reply_markup=language_markup()
        )
    else:
        await message.answer(
            text=_('Главное меню'),
            reply_markup=main_markup()
        )
        await RegisterForm.name.set()
