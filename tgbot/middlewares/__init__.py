from sqlalchemy.orm import sessionmaker

from .db import DbSessionMiddleware
from .language import Language
from aiogram import Dispatcher


def register_middlewares(dp: Dispatcher, session_fabric: sessionmaker):
    dp.middleware.setup(DbSessionMiddleware(session_fabric))
    dp.middleware.setup(Language(domain="messages", path="tgbot/locales", default="uz"))
