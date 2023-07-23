from telebot.types import Message
from database.init_db import DATABASE, db_lock
from utils.check_subscribe import check_subscribe
from loader import bot

@bot.message_handler(commands=["subscribe"])
def subscribe(message: Message):
    # Подписка на еженедельную рассылку в среду
    user_id = message.chat.id
    if not check_subscribe(user_id):
        with db_lock:
            DATABASE.cursor.execute("INSERT OR REPLACE INTO subscriptions (user_id, subscribed) VALUES (?, ?)", (user_id, 1))
            DATABASE.conn.commit()
        bot.reply_to(message, "Dude, вы успешно подписались на рассылку фото с жабой!\n"
                              "Ждите среды")
    else: bot.reply_to(message, "Dude, вы уже были подписаны на рассылку фото с жабой!\n"
                                "Два раза в одну рассылку не попасть")