import sqlite3
from loguru import logger


class BaseData:
    @logger.catch
    def __init__(self):
        # Путь к файлу базы данных SQLite
        self.db_file = 'subscriptions.db'

        # Создаем подключение к базе данных SQLite и получаем курсор для выполнения SQL-запросов
        self.conn = sqlite3.connect(self.db_file, check_same_thread=False)
        self.cursor = self.conn.cursor()

        # Создаем таблицу "subscriptions" в базе данных, если она не существует
        # Таблица содержит два столбца: user_id (идентификатор пользователя, является PRIMARY KEY)
        # и subscribed (флаг, указывающий на подписку пользователя, тип INTEGER)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS subscriptions
                          (user_id INTEGER PRIMARY KEY, subscribed INTEGER)''')

        # Применяем изменения в базе данных
        self.conn.commit()
