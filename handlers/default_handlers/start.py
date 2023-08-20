"""
Модуль обработчика команды /start для первого (или нет) запуска бота.

"""

from telebot.types import Message
from loguru import logger
from loader import bot




@logger.catch()
@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    """
    Обработчик команды /start для приветствия пользователя и предоставления информации о боте.

    Возвращает приветственное сообщение и список доступных команд пользователю.

    :param message: Объект сообщения от Telegram бота.
    :return: None
    """
    bot.reply_to(message, "Dude, вы вступили на верный путь!\n"
                          "Теперь вам всегда будет сопутствовать неудача за пропуск wednesday\n"
                          "Список команд: /help")