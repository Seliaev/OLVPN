"""
Модуль обработчика команды /unsubscribe для отписки от еженедельной рассылки в среду.

"""


from telebot.types import Message
from database.init_db import DATABASE, db_lock
from utils.check_subscribe import check_subscribe
from loader import bot
from loguru import logger

@logger.catch
@bot.message_handler(commands=["unsubscribe"])
def subscribe(message: Message):
    """
    Обработчик команды /unsubscribe для отписки от еженедельной рассылки в среду.

    Проверяет наличие подписки пользователя в базе данных функцией check_subscribe
    Если пользователь был подписан на рассылку, изменяет его статус подписки на 0 (отписан) в базе данных.
    Пользователь получит сообщение об успешной отписке. Если пользователь не был подписан, он получит сообщение
    о том, что отписка невозможна, так как он не был подписан ранее.

    :param message: Объект сообщения от Telegram бота.
    :return: None
    """
    user_id = message.chat.id
    if check_subscribe(user_id):
        with db_lock:
            DATABASE.cursor.execute("INSERT OR REPLACE INTO subscriptions (user_id, subscribed) VALUES (?, ?)", (user_id, 0))
            DATABASE.conn.commit()
        bot.reply_to(message, "Вы отписались от рассылки фото с жабой!\nНо зачем, не dude?"
                              "Давай снова - /subscribe")
    else: bot.reply_to(message, "Dude, вы и не были подписаны!\n"
                                "Пора подписаться - /subscribe")