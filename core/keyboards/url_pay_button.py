from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def url_pay_keyboard_build(url_payment: str, back_button: str) -> InlineKeyboardMarkup:
    """
    Генерирует клавиатуру для оплаты и проверки оплаты.

    :return: InlineKeyboardMarkup - Объект InlineKeyboardMarkup, содержащий клавиатуру.
    """
    text = f'💳 Оплатить'
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text=text, url=url_payment)
    keyboard_builder.button(text='🔎 Проверить оплату', callback_data='pay_check')
    keyboard_builder.button(text='🔙 Назад', callback_data=back_button)
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()