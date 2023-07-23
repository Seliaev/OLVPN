from telebot.types import Message

from loader import bot

@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    bot.reply_to(message, "Dude, вы вступили на верный путь!\n"
                          "Теперь вам всегда будет сопутствовать неудача за пропуск wednesday\n"
                          "Список команд: /help")