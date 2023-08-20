"""
Модуль обработки с schedule

"""

import schedule
from time import sleep

def schedule_checker() -> None:
    """
    Проверка времени рассылки и запуск функции при соответствии.

    Функция запускает бесконечный цикл, в котором вызывается метод `run_pending()` из модуля `schedule`
    для выполнения запланированных задач. После каждой итерации цикла, функция ожидает 1 секунду с помощью `sleep(1)`.

    """
    while True:
        schedule.run_pending()
        sleep(1)