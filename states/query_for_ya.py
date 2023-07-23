from telebot.handler_backends import State, StatesGroup

class QueryForYa(StatesGroup):
    query = State()
    start_page = State()