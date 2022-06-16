from aiogram.dispatcher.filters.state import StatesGroup, State


class RegisterForm(StatesGroup):
    name = State()
    surname = State()
    age = State()
    email = State()
    region = State()
    phone_number = State()

