from telebot.types import Message

from loader import bot

# Хндлер с текстовыми сообщения без указанного состояния
@bot.message_handler(state=None)
def bot_echo(message: Message):
    pass
