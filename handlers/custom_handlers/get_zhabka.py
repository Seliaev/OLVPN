from telebot.types import Message
from loguru import logger
from utils.get_meme_images import get_random_path_meme
from loader import bot


@logger.catch
@bot.message_handler(commands=["get_zhabka"])
def get_meme(message: Message):
    # Получаем случайную картинку из папки с жабами
    image_path = get_random_path_meme()
    if image_path is False:
        bot.send_message(message.chat.id, 'Картинок нет. Обратитесь к администратору.')
    # Отправляем изображение
    else:
        with open(image_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
