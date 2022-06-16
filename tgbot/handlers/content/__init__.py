from aiogram import Dispatcher

from .get_data import get_name, get_surname, get_age, get_email, get_region, get_phone
from tgbot.states.states import RegisterForm


def register_content(dp: Dispatcher):
    dp.register_message_handler(get_name, state=RegisterForm.name)
    dp.register_message_handler(get_surname, state=RegisterForm.surname)
    dp.register_message_handler(get_age, state=RegisterForm.age)
    dp.register_message_handler(get_email, state=RegisterForm.email, regexp=r"^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$")
    dp.register_message_handler(get_region, state=RegisterForm.region)
    dp.register_message_handler(get_phone, content_types=['contact'], state=RegisterForm.phone_number)
