from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from core.sql.function_db_user_vpn.users_vpn import get_promo_status


async def time_keyboard(id_user: int) -> InlineKeyboardMarkup:
    """
    Генерирует клавиатуру для выбора срока подписки.
    Есть проверка - выдавался ли пользователю промо-ключ, если да
    убирает кнопку "Промо"

    :return: InlineKeyboardMarkup - Объект InlineKeyboardMarkup, содержащий клавиатуру.
    """
    first_row = [
        InlineKeyboardButton(text='День', callback_data='day'),
        InlineKeyboardButton(text='Неделя', callback_data='week'),
        InlineKeyboardButton(text='Месяц', callback_data='month')
    ]
    second_row = [
        InlineKeyboardButton(text='Промо', callback_data='promo'),
        InlineKeyboardButton(text='Назад', callback_data='get_key')
    ]

    promo_status = await get_promo_status(account=id_user)
    if promo_status:
        second_row.pop(0)
    buttons = [
        first_row,
        second_row
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
