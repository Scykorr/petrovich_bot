from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from app.keyboards import get_number, registration, help_categories
from aiogram.enums import ParseMode
from main_info.token import passwd
from .states import Client
from datetime import datetime

router = Router()
user_pass = passwd
allowed_users = ['scykor', 'mm_operator_1', 'mm_operator_2', 'mm_operator_3',
                 'mm_operator_4', 'mm_operator_5', 'mm_operator_6',
                 'mm_operator_7', 'mm_operator_8', 'MM_operator_9',
                 'mm_operator_10', 'mm_operator_11', 'mm_operator_12',
                 'mm_operator_13', 'mm_operator_14', 'mm_operator_15',
                 'MM_Support_16', 'MM_Support8', 'mm_support18',
                 'mm_operator_19', 'mm_operator_20', 'MM_Support_21']


@router.message(CommandStart())
async def get_message(message: types.Message, state: FSMContext):
    username = message.from_user.username
    if username in allowed_users:
        await message.reply("👋 Здравствуйте!\n"
                            "Вы успешно авторизованы!\n"
                            "Введите id транзакции:")
        await state.set_state(Client.transaction_id)
    else:
        await message.reply("👋 Здравствуйте!\n"
                            "Авторизация не пройдена!\n"
                            "Для получения доступа к боту обратитесь к администратору!\n")
    # await message.reply(f'{username}👋 Здравствуйте! Я Ваш бот-помощник!\n'
    #                     'Для дальнейшей работу требуется пройти авторизацию.\n'
    #                     'Введите пароль.')
    # await state.set_state(Client.waiting_for_password)


# @router.message(Client.waiting_for_password)
# async def check_password(message: types.Message, state: FSMContext):
#     if message.text == user_pass:
#         await message.reply("Вы успешно авторизованы!\n"
#                             "Введите id транзакции:")
#         await state.set_state(Client.transaction_id)
#     else:
#         await message.reply("Неверный пароль. Попробуйте еще раз.")


@router.message(Client.transaction_id)
async def get_id(message: types.Message, state: FSMContext):
    if message.text == 'Выход':
        await message.answer('До свидания!👋')
        await state.clear()
    else:
        id_for_api = message.text
        res_response_blowfish = {
            "data": [
                {
                    "id": "20daad40-cba4-4687-a287-85e0e975dee5",
                    "created_at": "2025-02-11 01:14:23",
                    "updated_at": "2025-02-11 01:14:24",
                    "type_id": 1,
                    "type_text": "deposit",
                    "state_id": 1,
                    "state_text": "Created",
                    "state_final": False,
                    "participant_id": "404ae456-fb1d-4043-9e7b-a399f4d29cf3",
                    "participant_name": "TestAurisAccount",
                    "customer_id": "id-784693968623",
                    "customer_payment_id": "449bc546-e589-4aca-83fd-879694134546",
                    "source_amount_currency": "AZN",
                    "source_amount_value": "6000.00",
                    "destination_amount_currency": "AZN",
                    "destination_amount_value": "0",
                    "rate": "0",
                    "rate_source_currency": "AZN",
                    "rate_destination_currency": "AZN",
                    "provider": "pay4u",
                    "source_requisites": [
                        {
                            "bank_name": "sberbank",
                            "card_holder": "Сбер Картович",
                            "card_number": "1112121111111112"
                        }
                    ]
                }
            ],
            "success": True
        }
        res_response_external = {
            "data": [
                {
                    "id": "20daad40-cba4-4687-a287-85e0e975dee5",
                    "created_at": "2025-02-11 01:14:23",
                    "updated_at": "2025-02-11 01:14:24",
                    "type_id": 1,
                    "type_text": "deposit",
                    "state_id": 1,
                    "state_text": "Created",
                    "state_final": False,
                    "participant_id": "404ae456-fb1d-4043-9e7b-a399f4d29cf3",
                    "participant_name": "TestAurisAccount",
                    "customer_id": "id-784693968623",
                    "customer_payment_id": "449bc546-e589-4aca-83fd-879694134546",
                    "source_amount_currency": "AZN",
                    "source_amount_value": "6000.00",
                    "destination_amount_currency": "AZN",
                    "destination_amount_value": "0",
                    "rate": "0",
                    "rate_source_currency": "AZN",
                    "rate_destination_currency": "AZN",
                    "provider": "pay4u",
                    "source_requisites": [
                        {
                            "bank_name": "sberbank",
                            "card_holder": "Сбер Картович",
                            "card_number": "1112121111111112"
                        }
                    ]
                }
            ],
            "success": True
        }
        blowfish_id = res_response_blowfish["data"][0]['id']
        external_id = res_response_external["data"][0]['id']
        source_amount_value = res_response_blowfish["data"][0]['source_amount_value']
        parts = source_amount_value.split('.')
        integer_part = parts[0]
        decimal_part = parts[1]
        formatted_integer_part = ' '.join(
            [integer_part[max(i-3, 0):i] for i in range(len(integer_part), 0, -3)][::-1])
        source_amount_value = f"{formatted_integer_part}.{decimal_part}"
        source_amount_currency = res_response_blowfish["data"][0]['source_amount_currency']
        date_create = res_response_blowfish["data"][0]['created_at']
        date_obj = date_obj = datetime.strptime(
            date_create, "%Y-%m-%d %H:%M:%S")
        created_at_date = date_obj.strftime("%d.%m.%Y")
        created_at_time = date_obj.strftime("%H:%M:%S")
        provider = res_response_blowfish["data"][0]['provider']
        bank_name = res_response_blowfish["data"][0]['source_requisites'][0]['bank_name']
        card_holder = res_response_blowfish["data"][0]['source_requisites'][0]['card_holder']
        card_number = res_response_blowfish["data"][0]['source_requisites'][0]['card_number']
        result_text = f"Deposit 📥 Transaction 🔥Processing\n\n" + \
            f"Blowfish ID: <code>{blowfish_id}</code>\n" + \
            f"External ID: <code>{external_id}</code>\n\n" + \
            f"Amount: <u>{source_amount_value} {source_amount_currency}</u>\n" + \
            f"Date: <u>{created_at_date}</u>\n" + \
            f"Time (MSK): <u>{created_at_time}</u>\n\n" + \
            f"💱Provider: <u>{provider}</u>\n\n" + \
            f"👨‍💼Trader:\n" + \
            f"bank name: <u>{bank_name}</u>\n" + \
            f"card holder: <u>{card_holder}</u>\n" + \
            f"card number: <u>{card_number}</u>"
        await message.reply(result_text, parse_mode=ParseMode.HTML)
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
