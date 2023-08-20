"""
Модуль, содержащий обработчики сообщений для Telegram бота
Сообщения являются командой администратора, для обновления пака картинок.

"""


from telebot.types import Message
from images_update.ya_images_updater import ya_updater
from states.query_for_ya import QueryForYa
from config_data.config import ADMIN_ID
from loader import bot
from loguru import logger


@logger.catch
@bot.message_handler(commands=["update"])
def bot_update(message: Message):
    """
    Обработчик команды /update для обновления картинок с жабами.

    Если пользователь является администратором, он может ввести запрос на тему жаб для среды.
    Запрос сохраняется, и используется для обновления картинок с жабами на следующую среду.

    :param message: Объект сообщения от Telegram бота.
    :return: None
    """
    if message.chat.id in ADMIN_ID:
        bot.set_state(message.from_user.id, QueryForYa.query, message.chat.id)
        text = "Введите запрос на тему жаб для среды\n" \
               "Примеры: 'Это среда, мои чюваки', 'it's wednesday my dudes'"
        bot.send_message(message.from_user.id, text)

@logger.catch
@bot.message_handler(state=QueryForYa.query)
def get_query(message: Message):
    """
    Обработчик для получения запроса на поиск картинок с жабами.

    Пользователь вводит запрос на тему жаб для среды. Запрос сохраняется в состоянии чата
    и используется для поиска картинок с жабами на следующую среду.

    :param message: Объект сообщения от Telegram бота.
    :return: None
    """
    bot.send_message(message.from_user.id, f'Отлично, твой запрос: {message.text}.\n'
                                           f'Теперь введи начальную страницу для поиска. От 0 до 4')
    bot.set_state(message.from_user.id, QueryForYa.start_page, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['query'] = message.text

@logger.catch
@bot.message_handler(state=QueryForYa.start_page)
def get_query(message: Message):
    """
    Обработчик для получения начальной страницы поиска картинок с жабами.
    И в конечном итоге обновления картинок в функции ya_updater

    Пользователь вводит начальную страницу для поиска картинок с жабами (число от 0 до 4, почему 4? Просто так).
    Значение начальной страницы сохраняется в состоянии чата и используется для поиска картинок.
    Значения запроса и начальной страницы передаются в ya_updater, из нее возвращается True или False

    :param message: Объект сообщения от Telegram бота.
    :return: None
    """
    # Запрос для начальной страницы поиска
    if message.text.isdigit() and int(message.text) <= 4:
        bot.send_message(message.from_user.id, f'Начальная страница: {message.text}.')
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['start_page'] = int(message.text)
        bot.send_message(message.from_user.id, f'Теперь нужно подождать...')
        result_updater = ya_updater(query=data['query'], start_page=data['start_page'])
        if result_updater == True:
            bot.send_message(message.from_user.id, f'Картинки обновлены!')
        else:
            bot.send_message(message.from_user.id, f'Картинки не обновлены! Нужно проверить ошибки!')
        bot.delete_state(message.from_user.id, message.chat.id)
    else:
        bot.send_message(message.from_user.id, f'Вы должны ввести число! от 0 до 4')