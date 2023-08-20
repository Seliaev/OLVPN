"""
Модуль логов.

"""

from datetime import datetime
from loguru import logger
import os


def setup_logger() -> None:
    """
    Задание конфигурации логгера.

    Логи записываются в файл, который архивируется каждый день в 10:00 по времени сервера.
    Старый лог-файл архивируется.

    Формат логов: Время - Уровень информации - Сообщение

    :return: None
    """
    current_dir = os.getcwd()
    now = datetime.now()
    log_file = f'{current_dir}\\logs\\{now.strftime("%Y-%m-%d.json")}'
    logger.add(log_file, format="{time:YYYY-MM-DD HH:mm:ss.SSS} - {level} - {message}", rotation="10:00", retention=5,  compression="zip", serialize=True)

