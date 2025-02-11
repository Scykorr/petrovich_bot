from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from app.keyboards import get_number, registration, help_categories
from main_info.token import passwd
from .states import Client

router = Router()
user_pass = passwd

@router.message(CommandStart())
async def get_message(message: types.Message, state: FSMContext):
    await message.reply('👋 Здравствуйте! Я Ваш бот-помощник!\n'
                         'Для дальнейшей работу требуется пройти авторизацию.\n'
                        'Введите пароль.')
    await state.set_state(Client.waiting_for_password)

@router.message(Client.waiting_for_password)
async def check_password(message: types.Message, state: FSMContext):
    if message.text == user_pass:
        await message.reply("Вы успешно авторизованы!\n"
                            "Введите id транзакции:")
        await state.set_state(Client.transaction_id)
    else:
        await message.reply("Неверный пароль. Попробуйте еще раз.")


@router.message(Client.transaction_id)
async def get_id(message: types.Message, state: FSMContext):
    if message.text == 'Выход':
        await message.answer('До свидания!👋')
        await state.clear()
    else:
        id_for_api = message.text
        await message.reply(f"Deposit 📥 Transaction 🔥Processing\n\n"
                            f"Blowfish ID: 85a6979e-cf86-4777-9b7e-37f4748e3edb\n"
                            f"External ID: 456b6c26-192d-46ab-bab7-d47a12e28318\n\n"
                            f"Amount: 5 000 RUB\n"
                            f"Date: 10.02.2025\n"
                            f"Time (MSK): 11:21:07\n\n"
                            f"💹Provider: pay4u\n\n"
                            f"💱Trader:\n"
                            f"Name: Иван Сергеевич К.\n"
                            f"Requisites: 1234 5678 0001 0000")
        await message.answer('Введите id транзакции:')
        await state.set_state(Client.transaction_id)

#
# @router.message(Client.exit_working)
# async def exit_work(message: types.Message, state: FSMContext):



# @router.message(F.text == 'Введите id транзакции:')
# async def register(message: types.Message, state: FSMContext):
#     await state.set_state(Client.surname)
#     await message.answer('Введите Вашу Фамилию: ')
#
#
# @router.message(Client.surname)
# async def register_surname(message: types.Message, state: FSMContext):
#     await state.update_data(surname=message.text)
#     await state.set_state(Client.name)
#     await message.answer('Введите Ваше Имя: ')
#
#
# @router.message(Client.name)
# async def register_name(message: types.Message, state: FSMContext):
#     await state.update_data(name=message.text)
#     await state.set_state(Client.parent_name)
#     await message.answer('Введите Ваше Отчество: ')
#
#
# @router.message(Client.parent_name)
# async def register_parent_name(message: types.Message, state: FSMContext):
#     await state.update_data(parent_name=message.text)
#     await state.set_state(Client.birthday_date)
#     await message.answer('Введите Вашу дату рождения (образец: 01.01.1991): ')
#
#
# @router.message(Client.birthday_date)
# async def register_birthday_date(message: types.Message, state: FSMContext):
#     await state.update_data(birthday_date=message.text)
#     await state.set_state(Client.phone_number)
#     await message.answer('Нажмите на кнопку ниже, чтобы предоставить Ваш контактный номер телефона: ', reply_markup=get_number)
#
#
# @router.message(Client.phone_number, F.contact)
# async def register_number(message: types.Message, state: FSMContext):
#     await state.update_data(phone_number=message.contact.phone_number)
#     await state.set_state(Client.help_category)
#     await message.answer('Выберите одну из категорий: ', reply_markup=help_categories)
#
#
# @router.message(Client.help_category)
# async def register_help_category(message: types.Message, state: FSMContext):
#     await state.update_data(help_category=message.text)
#     data = await state.get_data()
#     await message.answer(f'Ваша Фамилия: {data["surname"]}\n'
#                          f'Ваше Имя: {data["name"]}\n'
#                          f'Ваше Отчество: {data["parent_name"]}\n'
#                          f'Ваша дата рождения: {data["birthday_date"]}\n'
#                          f'Номер телефона: {data["phone_number"]}\n'
#                          f'Категория: {data["help_category"]}'
#                          )
#     await state.clear()
