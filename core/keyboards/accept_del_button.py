from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def accept_del_keyboard() -> InlineKeyboardMarkup:
    """
    Генерирует клавиатуру для подтверждения или опровержения удаления ключа

    :return: InlineKeyboardMarkup - Объект InlineKeyboardMarkup, содержащий клавиатуру.
    """
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Подтверждаю', callback_data='del_key')
    keyboard_builder.button(text='Отмена', callback_data='get_key')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()
