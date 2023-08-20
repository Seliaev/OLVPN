from telebot.handler_backends import State, StatesGroup

class QueryForYa(StatesGroup):
    """
    Состояния чата для команды update к парсу яндекс.картинок.

    Содержит два состояния:
    - query: состояние, в котором ожидается ввод запроса для поиска картинок.
    - start_page: состояние, в котором ожидается ввод начальной страницы для поиска.

    """
    query = State()
    start_page = State()