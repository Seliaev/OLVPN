"""
Модуль обработчика команды /help для получения справки по командам бота(для пользователя).

"""

from telebot.types import Message
from loguru import logger
from config_data.config import DEFAULT_COMMANDS
from loader import bot

@logger.catch
@bot.message_handler(commands=["help"])
def bot_help(message: Message):
    """
    Обработчик команды /help для получения справки по командам бота (для пользователя).

    Выводит список доступных команд и их описания для пользователя.

    :param message: Объект сообщения от Telegram бота.
    :return: None
    """
    text = [f"/{command} - {desk}" for command, desk in DEFAULT_COMMANDS]
    bot.reply_to(message, "\n".join(text))
