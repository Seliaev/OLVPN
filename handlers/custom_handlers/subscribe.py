"""
Модуль обработчика команды /subscribe для подписки на еженедельную рассылку в среду.

"""

from telebot.types import Message
from database.init_db import DATABASE, db_lock
from utils.check_subscribe import check_subscribe
from loader import bot
from loguru import logger

@logger.catch
@bot.message_handler(commands=["subscribe"])
def subscribe(message: Message):
    """
    Обработчик команды /subscribe для подписки на еженедельную рассылку в среду.

    Проверяет наличие подписки пользователя в базе данных функцией check_subscribe
    Если пользователь еще не подписан на рассылку, добавляет его идентификатор в базу данных,
    указывая флаг подписки на 1. Пользователь получит сообщение о успешной подписке.
    Если пользователь уже подписан, он получит сообщение об уже существующей подписке.

    :param message: Объект сообщения от Telegram бота.
    :return: None
    """
    user_id = message.chat.id
    if not check_subscribe(user_id):
        with db_lock:
            DATABASE.cursor.execute("INSERT OR REPLACE INTO subscriptions (user_id, subscribed) VALUES (?, ?)", (user_id, 1))
            DATABASE.conn.commit()
        bot.reply_to(message, "Dude, вы успешно подписались на рассылку фото с жабой!\n"
                              "Ждите среды")
    else: bot.reply_to(message, "Dude, вы уже были подписаны на рассылку фото с жабой!\n"
                                "Два раза в одну рассылку не попасть")