from aiogram.types import Message
from tgbot.data.data import _
from tgbot.keyboards.inline.language_keyboard import language_markup
from tgbot.service.repo.repository import SQLAlchemyRepos
from tgbot.service.repo.user_repo import UserRepo


async def user_start(message: Message, repo: SQLAlchemyRepos):
    user = repo.get_repo(UserRepo)
    if await user.get_user(user_id=message.from_user.id) is None:
        await message.answer(
            text=_('Здравствуйте! Выберите необходимый язык'),
            reply_markup=language_markup()
        )
    else:
        pass
