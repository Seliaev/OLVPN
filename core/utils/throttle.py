import functools
from datetime import datetime


def throttle(seconds: int) -> callable:
    """
    Декоратор для ограничения частоты нажатия на клавиатуру.

    :param seconds: float - Время в секундах, которое должно пройти между вызовами функции.
    :return: callable - Декоратор, который применяется к асинхронной функции.
    """
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            current_time = datetime.now()

            if 'last_call' not in wrapper.__dict__:
                # Если это первый вызов, устанавливаем время последнего вызова
                wrapper.last_call = current_time
            else:
                # Проверяем, прошло ли достаточно времени с момента последнего вызова
                time_since_last_call = current_time - wrapper.last_call
                if time_since_last_call.total_seconds() < seconds:
                    await args[0].answer(f"Частые нажатия\nНужно ждать еще {round(seconds - time_since_last_call.total_seconds(), 2)} сек", show_alert=True)
                    return
                # Обновляем время последнего вызова
                wrapper.last_call = current_time
            # Выполняем асинхронную функцию
            result = await func(*args, **kwargs)
            return result
        return wrapper
    return decorator