from telebot.handler_backends import State, StatesGroup

class QueryForYa(StatesGroup):
    # Состояния чата для команды update у яндекс.картинок
    query = State()
    start_page = State()