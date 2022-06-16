from aiogram import types
from tgbot.data.data import _
from tgbot.keyboards.default.main_keyboard import main_markup
from tgbot.service.repo.repository import SQLAlchemyRepos
from tgbot.service.repo.user_repo import UserRepo
from tgbot.states.states import RegisterForm


async def language_handler(query: types.CallbackQuery, callback_data: dict, repo: SQLAlchemyRepos):
    language_code = callback_data.get('language_code')
    user = repo.get_repo(UserRepo)
    if await user.get_user(user_id=query.from_user.id) is None:
        await user.add_user(
            user_id=query.from_user.id,
            name=query.from_user.full_name,
            username=query.from_user.username,
            language=language_code
        )
    else:
        await user.update_language(user_id=query.from_user.id, language=language_code)
    await query.answer()
    await query.message.delete()
    await query.message.answer(
        text=_('Главное меню', locale=language_code),
        reply_markup=main_markup(
            locale=language_code
        )
    )
    await query.message.answer(
        text=_('<b>Шаг 1.</b>\n\n'
               'Введите свое имя'),
        reply_markup=types.InlineKeyboardMarkup(
            row_width=1,
            inline_keyboard=[
                [types.InlineKeyboardButton(text=_('❌ Отмена'), callback_data='cancel')]
            ]
        )
    )
    await RegisterForm.name.set()

