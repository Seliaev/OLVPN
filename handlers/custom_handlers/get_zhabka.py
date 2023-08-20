"""
Модуль обработчика команды /get_zhabka для получения случайной картинки с жабой.

"""

from telebot.types import Message
from loguru import logger
from utils.get_meme_images import get_random_path_meme
from loader import bot


@logger.catch
@bot.message_handler(commands=["get_zhabka"])
def get_meme(message: Message):
    """
    Обработчик команды /get_zhabka для получения случайной картинки с жабой.

    Если в папке с жабами есть картинки, то выбирает случайную картинку ( функция get_random_path_meme ) и отправляет ее пользователю.
    Если их нет, отправляет об этом сообщение пользователю.

    :param message: Объект сообщения от Telegram бота.
    :return: None
    """
    image_path = get_random_path_meme() # Получаем случайную картинку из папки с жабами
    if image_path is False:
        bot.send_message(message.chat.id, 'Картинок нет. Обратитесь к администратору.')
    # Отправляем изображение
    else:
        with open(image_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
