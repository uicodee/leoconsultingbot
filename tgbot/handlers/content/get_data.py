from aiogram import types
from aiogram.dispatcher import FSMContext

from tgbot.data.data import _
from tgbot.service.repo.region_repo import RegionRepo
from tgbot.service.repo.repository import SQLAlchemyRepos
from tgbot.states.states import RegisterForm


async def get_name(message: types.Message, state: FSMContext):
    name = message.text
    if not name.isdigit():
        await state.update_data(name=name)
        await message.answer(
            text=_('Введите вашу фамилию'),
            reply_markup=types.InlineKeyboardMarkup(
                row_width=1,
                inline_keyboard=[
                    [types.InlineKeyboardButton(text=_('❌ Отмена'), callback_data='cancel')]
                ]
            )
        )
        await RegisterForm.surname.set()
    else:
        await message.answer(
            text=_('⚠️ Вводите данные в правильном формате')
        )


async def get_surname(message: types.Message, state: FSMContext):
    surname = message.text
    if not surname.isdigit():
        await state.update_data(surname=surname)
        await message.answer(
            text=_('Введите ваш возраст. Мы принимаем заявки начиная от 18 лет'),
            reply_markup=types.InlineKeyboardMarkup(
                row_width=1,
                inline_keyboard=[
                    [types.InlineKeyboardButton(text=_('❌ Отмена'), callback_data='cancel')]
                ]
            )
        )
        await RegisterForm.age.set()
    else:
        await message.answer(
            text=_('⚠️ Вводите данные в правильном формате')
        )


async def get_age(message: types.Message, state: FSMContext, repo: SQLAlchemyRepos):
    age = message.text
    if age.isdigit():
        if int(age) < 18:
            await message.answer(
                text=_('⚠️ Мы принимаем заявки только от 18 лет')
            )
        else:
            await state.update_data(age=age)
            region = repo.get_repo(RegionRepo)
            regions = await region.get_regions()
            keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=True)
            for r in regions:
                keyboard.insert(types.KeyboardButton(text=r.region_name))
            await message.answer(
                text=_('Выберите ваш регион с помощью кнопок ниже'),
                reply_markup=keyboard,
            )
            await RegisterForm.region.set()
    else:
        await message.answer(
            text=_('⚠️ Вводите данные в правильном формате')
        )


async def get_region(message: types.Message, repo: SQLAlchemyRepos, state: FSMContext):
    region = message.text
    regions = await repo.get_repo(RegionRepo).get_regions()
    regions = [x.region_name for x in regions]
    if region not in regions:
        await message.answer(
            text=_('⚠️ Выбирайте только с помощью кнопок')
        )
    else:
        await state.update_data(region=region)
        await message.answer(
            text=_('Отправьте номер телефона с помощью кнопок ниже'),
            reply_markup=types.ReplyKeyboardMarkup(
                row_width=1,
                keyboard=[[types.KeyboardButton(text=_('📞 Отправить номер телефона'), request_contact=True)]],
                resize_keyboard=True,
                one_time_keyboard=True
            )
        )
        await RegisterForm.phone_number.set()


async def get_phone(message: types.Message, repo: SQLAlchemyRepos, state: FSMContext):
    phone_number = message.contact.phone_number
    await state.update_data(phone_number=phone_number)
    data = await state.get_data()
    await message.answer(
        text=_('❗️ Еще раз перепроверьте свои данные затем потдвердите ваше действие\n\n'
               '<b>Имя:</b> {name}\n'
               '<b>Фамилия:</b> {surname}\n'
               '<b>Возраст:</b> {age}\n'
               '<b>Регион:</b> {region}\n'
               '<b>Номер телефона:</b> {phone_number}').format(
            name=data.get('name'),
            surname=data.get('surname'),
            age=data.get('age'),
            email=data.get('email'),
            region=data.get('region'),
            phone_number=phone_number
        ),
        reply_markup=types.InlineKeyboardMarkup(
            row_width=1,
            inline_keyboard=[
                [types.InlineKeyboardButton(text=_('✅ Подтвердить'), callback_data='confirm')],
                [types.InlineKeyboardButton(text=_('❌ Отмена'), callback_data='cancel')],
            ]
        )
    )
