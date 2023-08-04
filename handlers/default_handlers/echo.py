from telebot.types import Message
from loguru import logger
from loader import bot

@logger.catch
@bot.message_handler(state=None)
def bot_echo(message: Message):
    # Текстовые сообщения без указанного состояния
    pass
