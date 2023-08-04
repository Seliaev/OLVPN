from telebot.types import BotCommand
from config_data.config import DEFAULT_COMMANDS


def set_commands(bot) -> None:
    # Установка в бота списка используемых команд
    bot.set_my_commands(
        [BotCommand(*i) for i in DEFAULT_COMMANDS]
    )
