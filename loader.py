"""
Модуль запуска бота

"""

from telebot import TeleBot
from telebot.storage import StateMemoryStorage
from config_data import config

storage = StateMemoryStorage()
config.setup_env()
config.setup_admin_id()
bot = TeleBot(token=config.BOT_TOKEN, state_storage=storage)
