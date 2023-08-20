"""
Модуль, содержащий класс BaseData для работы с базой данных SQLite для управления подписками пользователей.

Этот модуль создает и подключается к базе данных SQLite, а также содержит класс BaseData с методами
для работы с подписками пользователей.

"""

import sqlite3
from loguru import logger

class BaseData:
    """
    Класс для работы с базой данных SQLite для управления подписками пользователей.

    """

    @logger.catch
    def __init__(self) -> None:
        """
        Конструктор класса.

        Инициализирует объект для работы с базой данных SQLite. Создает подключение к базе данных
        и получает курсор для выполнения SQL-запросов.

        :return: None
        """

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
