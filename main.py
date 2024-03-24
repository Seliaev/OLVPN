import asyncio
import multiprocessing

from core import bot, check_time_subscribe


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


if __name__ == "__main__":
    """
    Запуск модулей через multiprocessing
    """
    bot_th = multiprocessing.Process(target=run_bot)
    plan_th = multiprocessing.Process(target=run_checker)
    bot_th.start()
    plan_th.start()
    bot_th.join()
    plan_th.join()





