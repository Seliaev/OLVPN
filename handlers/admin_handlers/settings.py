from telebot.types import Message

from config_data.config import ADMIN_ID
from loader import bot

@bot.message_handler(commands=["settings"])
def bot_help(message: Message):
    print(ADMIN_ID)
    print(message.chat.id)
    if message.chat.id in ADMIN_ID:
        text = 'Настройки в разработке'
        # Добавить редактирование времени рассылки
        # Добавить редактирование админов, вывести админов в БД
        # Добавить отображение логов ошибок, добавить логи ошибок
        bot.reply_to(message, text)
