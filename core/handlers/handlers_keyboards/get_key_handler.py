from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup

from core.keyboards.choise_region_button import choise_region_keyboard
from core.keyboards.my_key_button import my_key_keyboard
from core.sql.function_db_user_vpn.users_vpn import get_user_data_from_table_users, get_region_server
from core.utils.build_pay import build_pay
from core.utils.create_view import create_answer_from_html
from core.utils.get_region_name import get_region_name_from_json


async def choise_region(call: CallbackQuery, state: FSMContext) -> (str, InlineKeyboardMarkup):
    """
    Обработчик для получения ключа.
    Отправка на выбор продолжительности действия ключа

    :param call: CallbackQuery - Объект CallbackQuery.
    :param state: FSMContext - Объект FSMContext.
    :return: Текст ответа и клавиатура.
    """
    name_temp = call.data
    content = await create_answer_from_html(name_temp=name_temp)
    await state.update_data(pay=(None, None))
    return content, choise_region_keyboard()


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
                region = await get_region_server(account=id_user)
                region_name = await get_region_name_from_json(region=region)
                content = await create_answer_from_html(name_temp=name_temp, user_key=user_data.key,
                                                        untill_date=untill_date, region_name=region_name)
                return content, my_key_keyboard()
    content = f'У вас нет ключа, но вы можете его купить\nВыберите регион'
    return content, choise_region_keyboard()
