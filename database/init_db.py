from .config_db import BaseData
import threading

# Инициализация базы данных
DATABASE = BaseData()

# Блокировка потока для защиты доступа к базе данных
db_lock = threading.Lock()
