from datetime import datetime
from loguru import logger
import os


def setup_logger():
    # Задание конфигурации логгера
    current_dir = os.getcwd()
    now = datetime.now()
    log_file = f'{current_dir}\\logs\\{now.strftime("%Y-%m-%d.json")}'
    logger.add(log_file, format="{time:YYYY-MM-DD HH:mm:ss.SSS} - {level} - {message}", rotation="10:00", retention=5,  compression="zip", serialize=True)
    # Логи архивируются каждый день в 10:00 по времени серврера. Старый лог-файл архивируется в ZIP-файл

