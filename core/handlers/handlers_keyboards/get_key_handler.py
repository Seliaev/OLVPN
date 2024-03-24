from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup

from core.keyboards.start_button import start_keyboard
from core.keyboards.time_button import time_keyboard
from core.sql.users_vpn import get_user_data_from_table_users
from core.utils.build_pay import build_pay
from core.utils.create_view import create_answer_from_html


async def get_key(call: CallbackQuery, state: FSMContext) -> (str, InlineKeyboardMarkup):
    """
    Обработчик для получения ключа.
    Отправка на выбор продолжительности действия ключа

    :param call: CallbackQuery - Объект CallbackQuery.
    :param state: FSMContext - Объект FSMContext.
    :return: Текст ответа и клавиатура.
    """
    id_user = call.from_user.id
    name_temp = call.data
    content = await create_answer_from_html(name_temp=name_temp)
    return content, await time_keyboard(id_user=id_user)


async def day_key(call: CallbackQuery, state: FSMContext) -> (str, InlineKeyboardMarkup):
    """
    Обработчик для получения ключа на день.
    Отправка на страницу оплаты

    :param call: CallbackQuery - Объект CallbackQuery.
    :param state: FSMContext - Объект FSMContext.
    :return: Текст ответа и клавиатура.
    """
    id_user = call.from_user.id
    amount = 7
    day_count = 1
    word_days = "день"
    content, url_pay_keyboard = await build_pay(state, id_user, amount, day_count, word_days)
    return content, url_pay_keyboard


async def week_key(call: CallbackQuery, state: FSMContext) -> (str, InlineKeyboardMarkup):
    """
    Обработчик для получения ключа на неделю.
    Отправка на страницу оплаты

    :param call: CallbackQuery - Объект CallbackQuery.
    :param state: FSMContext - Объект FSMContext.
    :return: Текст ответа и клавиатура.
    """
    id_user = call.from_user.id
    amount = 40
    day_count = 7
    word_days = "дней"
    content, url_pay_keyboard = await build_pay(state, id_user, amount, day_count, word_days)
    return content, url_pay_keyboard


async def month_key(call: CallbackQuery, state: FSMContext) -> (str, InlineKeyboardMarkup):
    """
    Обработчик для получения ключа на месяц.
    Отправка на страницу оплаты

    :param call: CallbackQuery - Объект CallbackQuery.
    :param state: FSMContext - Объект FSMContext.
    :return: Текст ответа и клавиатура.
    """
    id_user = call.from_user.id
    amount = 150
    day_count = 30
    word_days = "дней"
    content, url_pay_keyboard = await build_pay(state, id_user, amount, day_count, word_days)
    return content, url_pay_keyboard


async def my_key(call: CallbackQuery, state: FSMContext) -> (str, InlineKeyboardMarkup):
    """
    Обработчик для кнопки "Мой ключ".
    Получение ключа, если он есть

    :param call: CallbackQuery - Объект CallbackQuery.
    :param state: FSMContext - Объект FSMContext.
    :return: Текст ответа и клавиатура.
    """
    id_user = call.from_user.id
    user_data = await get_user_data_from_table_users(account=id_user)
    name_temp = call.data
    if user_data:
        untill_date = user_data.date
        if untill_date:
            untill_date = untill_date.strftime('%d.%m.%Y - %H:%M')
            if untill_date != '01.01.2000 - 00:00':
                content = await create_answer_from_html(name_temp=name_temp, user_key=user_data.key, untill_date=untill_date)
                return content, start_keyboard()
    content = f'У вас нет ключа'
    return content, await time_keyboard(id_user=id_user)
