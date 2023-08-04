import re

def is_valid_time(time_str) -> bool:
    # Регулярное выражение для проверки формата времени "часы:минуты"
    time_regex = re.compile(r'^([01]\d|2[0-3]):[0-5]\d$')
    if not time_regex.match(time_str):
        return False
    hours, minutes = map(int, time_str.split(':'))
    if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
        return False
    return True
