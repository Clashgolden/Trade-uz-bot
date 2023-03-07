from aiogram.dispatcher.filters.state import State, StatesGroup

class register(StatesGroup):
    name = State()
    number = State()
    lvl = State()