from database.init_db import DATABASE, db_lock
from utils.get_meme_images import get_random_path_meme
from loader import bot
from telebot.types import Message


def send_zhabka(message: Message):
    # Получаем список подписанных пользователей из базы данных
    with db_lock:
        DATABASE.cursor.execute("SELECT user_id FROM subscriptions WHERE subscribed = 1")
        result = DATABASE.cursor.fetchall()
        subscribed_users = [row[0] for row in result]
    # Отправляем фото каждому подписанному пользователю
    for user_id in subscribed_users:
        # Получаем случайную картинку из папки с жабами
        image_path = get_random_path_meme()
        if image_path is False:
            bot.send_message(message.chat.id, 'Картинок нет. Обратитесь к администратору.')
        # Открываем картинку
        else:
            with open(image_path, 'rb') as photo:
                # Отправляем изображение каждому пользователю
                bot.send_photo(user_id, photo)
    return True