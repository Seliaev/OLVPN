from core.keyboards.start_button import start_keyboard


async def back_key(*args) -> tuple:
    """
    Обработчик для кнопки "Назад".

    :return: Текст ответа и клавиатура.
    """
    text = '<b>Выберите нужное меню</b>'
    return text, start_keyboard()
