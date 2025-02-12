from aiogram.fsm.state import State, StatesGroup


class Client(StatesGroup):
    waiting_for_password = State()
    transaction_id = State()
    exit_working = State()

