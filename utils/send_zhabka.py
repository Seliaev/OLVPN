from database.init_db import DATABASE, db_lock
from utils.get_meme_images import get_random_path_meme
from loader import bot
from telebot.types import Message


def send_zhabka(message: Message) -> bool:
    """
    Отправление картинки подписанным пользователям по расписанию и из schedule

    Функция получает список подписанных пользователей из базы данных и отправляет случайную картинку
    из папки каждому подписчику.

    Если папка картинок пустая, сообщает об этом пользователю.

    :param message: Сообщение из телеграма
    :return: Всегда возвращает True после выполнения
    """
    with db_lock:
        #Проверка подписки пользователя в БД
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