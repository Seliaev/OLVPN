import sqlite3

class BaseData:
    def __init__(self):
        # Путь к файлу базы данных SQLite
        self.db_file = 'subscriptions.db'

        # Создаем таблицу в базе данных, если она не существует
        self.conn = sqlite3.connect(self.db_file, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS subscriptions
                          (user_id INTEGER PRIMARY KEY, subscribed INTEGER)''')
        self.conn.commit()
