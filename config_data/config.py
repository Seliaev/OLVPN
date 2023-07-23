import os
from dotenv import load_dotenv, find_dotenv

if find_dotenv():
    load_dotenv()
else:
    exit("Отсутствует файл .env, создайте его по примеру .env.template")

BOT_TOKEN = os.getenv("TLG_TOKEN")
MEME_IMAGES_FOLDER = 'images'
ADMIN_ID = [int(os.getenv("TLG_ADMIN"))]

DEFAULT_COMMANDS = (
    ("start", "Dude, это начало"),
    ("help", "Справка, dude"),
    ("get_zhabka", "Получить жабку просто так, вне очереди"),
    ("subscribe", "Подписаться на wednesday, dude"),
    ("unsubscribe", "Бесполезная команда"),
)
