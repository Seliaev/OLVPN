import asyncio
import multiprocessing
import sys
import signal

from core import bot, check_time_subscribe
from logs.log_main import RotatingFileLogger

logger = RotatingFileLogger()
logger_payments = RotatingFileLogger(config_file='logs/log_settings_payments.json')


def run_bot() -> None:
    """
    Для запуска процесса бота
    :return: None
    """
    asyncio.run(bot.start_bot())


def run_checker() -> None:
    """
    Для запуска процесса проверки подписки
    :return: None
    """
    asyncio.run(check_time_subscribe.main_check_subscribe())


def stop_application(signum: int, frame: int) -> None:
    """
    Обработчик сигнала остановки приложения
    :param signum: Номер сигнала
    :param frame: Текущий фрейм стека
    :return: None
    """
    logger_payments.log('warning', 'Логгер остановлен')
    logger.log('info', 'Приложение остановлено')
    sys.exit(0)


if __name__ == "__main__":
    """
    Запуск модулей через multiprocessing
    """
    signal.signal(signal.SIGINT, stop_application)

    logger.log('info', 'Запуск приложения')
    logger_payments.log('warning', 'Запуск логгера payments')
    bot_th = multiprocessing.Process(target=run_bot)
    plan_th = multiprocessing.Process(target=run_checker)
    bot_th.start()
    plan_th.start()
    bot_th.join()
    plan_th.join()


# Добавить получение ссылки (или файл) сразу на приложение по запросу платформы
# Проверить работу выбора региона, добавить возможность добавления регионов из бота
# Добавить проработку в случае отсутвия региона. Убрать его из env