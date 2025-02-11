from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

registration = get_number = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Авторизация')]],
    input_field_placeholder='Введите пароль и нажмите на кнопку для авторизации'
)

get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Отправить номер', request_contact=True)]],
                                 resize_keyboard=True)

help_categories = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Выплата')],
                                              [KeyboardButton(text='Эвакуация')],
                                              [KeyboardButton(text='Сертификат')]],
                                    input_field_placeholder='Выберите требуемый пункт меню...')
