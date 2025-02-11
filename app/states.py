from aiogram.fsm.state import State, StatesGroup


class Client(StatesGroup):
    waiting_for_password = State()
    transaction_id = State()
    exit_working = State()
    # name = State()
    # surname = State()
    # parent_name = State()
    # birthday_date = State()
    # phone_number = State()
    # help_category = State()

