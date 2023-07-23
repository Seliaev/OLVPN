from telebot.types import Message
from images_update.ya_images_updater import ya_updater
from states.query_for_ya import QueryForYa
from config_data.config import ADMIN_ID
from loader import bot

@bot.message_handler(commands=["update"])
def bot_update(message: Message):
    # Обновление картинок с жабами
    if message.chat.id in ADMIN_ID:
        bot.set_state(message.from_user.id, QueryForYa.query, message.chat.id)
        text = "Введите запрос на тему жаб для среды\n" \
               "Примеры: 'Это среда, мои чюваки', 'it's wednesday my dudes'"
        bot.send_message(message.from_user.id, text)

@bot.message_handler(state=QueryForYa.query)
def get_query(message: Message):
    # Запрос для поиска картинок
    bot.send_message(message.from_user.id, f'Отлично, твой запрос: {message.text}.\n'
                                           f'Теперь введи начальную страницу для поиска. От 0 до 4')
    bot.set_state(message.from_user.id, QueryForYa.start_page, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['query'] = message.text

@bot.message_handler(state=QueryForYa.start_page)
def get_query(message: Message):
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