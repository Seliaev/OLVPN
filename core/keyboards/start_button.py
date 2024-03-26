from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def start_keyboard() -> InlineKeyboardMarkup:
    """
    Генерирует клавиатуру для стартового меню.

    :return: InlineKeyboardMarkup - Объект InlineKeyboardMarkup, содержащий клавиатуру.
    """
    link_instruction = f"https://telegra.ph/Instrukciya-k-OLVPN-03-13-2"
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Ключ', callback_data='get_key')
    keyboard_builder.button(text='Инструкция', url=link_instruction)
    keyboard_builder.button(text='Приложение', callback_data='get_link_to_app')
    keyboard_builder.button(text='Удалить ключ', callback_data='ask_del_key')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()
