from telebot.types import Message
from loguru import logger
from loader import bot

@logger.catch()
@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    # Стартовая команда для пользователя
    bot.reply_to(message, "Dude, вы вступили на верный путь!\n"
                          "Теперь вам всегда будет сопутствовать неудача за пропуск wednesday\n"
                          "Список команд: /help")