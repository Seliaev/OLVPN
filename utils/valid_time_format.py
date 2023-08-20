"""
Модуль проверки корректности введенного времени

"""

import re

def is_valid_time(time_str) -> bool:
    """
    Проверка, является ли переданная строка допустимым временем в формате "часы:минуты".

    Функция использует регулярное выражение для проверки формата времени и допустимого диапазона часов (0-23) и минут (0-59).

    :param time_str: Строка с временем в формате "часы:минуты"
    :return: True, если переданная строка является допустимым временем, иначе False
    """
    time_regex = re.compile(r'^([01]\d|2[0-3]):[0-5]\d$')
    if not time_regex.match(time_str):
        return False
    hours, minutes = map(int, time_str.split(':'))
    if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
        return False
    return True
