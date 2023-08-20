from utils.schedule_checker import schedule_checker, schedule
from utils.send_zhabka import send_zhabka
from loader import bot
import handlers  # noqa
from utils.set_commands import set_commands
from telebot.custom_filters import StateFilter
from threading import Thread
from logs.log_config import setup_logger
from loguru import logger


setup_logger() # Конфигурация логгера

@logger.catch
def main() -> None:
    """
    Основная функция для запуска бота и его функций.

    Функция выполняет следующие шаги:
    1. Добавление пользовательского фильтра состояния.
    2. Установка команд для бота.
    3. Запуск расписания для отправки рассылки в среду.
    4. Запуск потока для проверки времени расписания.
    5. Запуск бесконечного опросчика бота.

    :return: None
    """
    bot.add_custom_filter(StateFilter(bot))
    set_commands(bot)
    schedule.every().wednesday.at("00:00").do(send_zhabka)
    Thread(target=schedule_checker).start()
    bot.infinity_polling()


if __name__ == "__main__":
    main()  # Запуск бота
