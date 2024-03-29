from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def my_key_keyboard() -> InlineKeyboardMarkup:
    """
    Генерирует клавиатуру при запросе ключа пользователя.

    :return: InlineKeyboardMarkup - Объект InlineKeyboardMarkup, содержащий клавиатуру.
    """
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Удалить ключ', callback_data='ask_del_key')
    keyboard_builder.button(text='Назад', callback_data='back')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()
