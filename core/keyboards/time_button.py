from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def time_keyboard() -> InlineKeyboardMarkup:
    """
    Генерирует клавиатуру для выбора срока подписки.

    :return: InlineKeyboardMarkup - Объект InlineKeyboardMarkup, содержащий клавиатуру.
    """
    buttons = [
        [
            InlineKeyboardButton(text='День', callback_data='day'),
            InlineKeyboardButton(text='Неделя', callback_data='week'),
            InlineKeyboardButton(text='Месяц', callback_data='month')
        ],
        [
            InlineKeyboardButton(text='Мой ключ', callback_data='my_key'),
            InlineKeyboardButton(text='Промо', callback_data='promo'),
            InlineKeyboardButton(text='Назад', callback_data='back')
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
