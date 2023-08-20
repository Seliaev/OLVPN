"""
Модуль установки команд для бота

"""

from telebot.types import BotCommand
from config_data.config import DEFAULT_COMMANDS


def set_commands(bot) -> None:
    """
    Установка списка команд в бот.
    Функция устанавливает в бот список команд, используя переданный список команд DEFAULT_COMMANDS.
    :param bot: Экземпляр бота
    :return: None
    """
    bot.set_my_commands(
        [BotCommand(*i) for i in DEFAULT_COMMANDS]
    )
