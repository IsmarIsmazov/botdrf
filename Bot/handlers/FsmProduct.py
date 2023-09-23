from aiogram.dispatcher.filters.state import State, StatesGroup


class ProductState(StatesGroup):
    start = State()
    random_product = State()
