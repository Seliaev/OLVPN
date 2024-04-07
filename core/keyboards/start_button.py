from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def start_keyboard() -> InlineKeyboardMarkup:
    """
    Генерирует клавиатуру для стартового меню.

    :return: InlineKeyboardMarkup - Объект InlineKeyboardMarkup, содержащий клавиатуру.
    """
    link_instruction = f"https://telegra.ph/Instrukciya-k-OLVPN-03-13-2"
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='🔑 Мой ключ', callback_data='my_key')
    keyboard_builder.button(text='💳 Купить ключ', callback_data='get_key')
    keyboard_builder.button(text='📚 Инструкция', url=link_instruction)
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()