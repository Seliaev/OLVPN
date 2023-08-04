import os
from dotenv import load_dotenv, find_dotenv

# Проверяем наличие файла .env и загружаем его содержимое в переменные среды, если он найден
if find_dotenv():
    load_dotenv()
else:
    exit("Отсутствует файл .env, создайте его по примеру .env.template")

# Получаем токен бота из переменной среды TLG_TOKEN и сохраняем его в переменную BOT_TOKEN
BOT_TOKEN = os.getenv("TLG_TOKEN")

# Указываем папку, где хранятся изображения для мемов
MEME_IMAGES_FOLDER = 'images'

# Создаем пустой список для хранения идентификаторов администраторов
ADMIN_ID = []

# Получаем идентификатор администратора из переменной среды TLG_ADMIN и добавляем его в список ADMIN_ID
ADMIN_ID.append(int(os.getenv("TLG_ADMIN")))

# Определяем стандартные команды для бота в виде кортежа кортежей
DEFAULT_COMMANDS = (
    ("start", "Dude, это начало"),
    ("help", "Справка, dude"),
    ("get_zhabka", "Получить жабку просто так, вне очереди"),
    ("subscribe", "Подписаться на wednesday, dude"),
    ("unsubscribe", "Бесполезная команда"),
)
