from aiogram.fsm.state import State, StatesGroup


class Client(StatesGroup):
    transaction_id = State()
