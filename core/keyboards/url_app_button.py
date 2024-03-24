from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def url_app_keyboard() -> InlineKeyboardMarkup:
    """
    Генерирует клавиатуру для отправки ссылки на скачивание приложения.

    :return: InlineKeyboardMarkup - Объект InlineKeyboardMarkup, содержащий клавиатуру.
    """
    link = f"https://getoutline.org/ru/get-started/#step-3"
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Скачать приложение', url=link)
    keyboard_builder.button(text='Назад', callback_data='back')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()
