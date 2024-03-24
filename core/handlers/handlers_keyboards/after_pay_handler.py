from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from core.api_s.api_youkassa.youkassa_api import check_payment
from core.keyboards.start_button import start_keyboard
from core.keyboards.url_pay_button import url_pay_keyboard_build
from core.sql.users_payments import add_payment_to_db
from core.utils.create_view import create_answer_from_html
from core.utils.get_key_utils import get_future_date, get_ol_key_func


async def after_pay(call: CallbackQuery, state: FSMContext) -> str:
    """
    Обработчик после успешной проверки оплаты.

    :param call: CallbackQuery - Объект CallbackQuery.
    :param state: FSMContext - Объект FSMContext.
    :return: Текст ответа и клавиатура.
    """
    name_temp = 'responce_key'
    data = await state.get_data()
    add_day = data.get('day_count', 0)
    untill_date = get_future_date(add_day=add_day)
    key_user = await get_ol_key_func(call=call, untill_date=untill_date)
    content = await create_answer_from_html(name_temp=name_temp, key_user=key_user.access_url, untill_date=untill_date)
    return content


async def pay_check_key(call: CallbackQuery, state: FSMContext) -> tuple:
    """
    Обработчик проверки оплаты (ручная проверка).
    В случае удачи отправка на генерацию ответа с данными в after_pay
    и сохранение записи о покупке в БД.


    :param call: CallbackQuery - Объект CallbackQuery.
    :param state: FSMContext - Объект FSMContext.
    :return: Текст ответа и клавиатура.
    """
    data = await state.get_data()
    payment_url, payment = data.get('pay', (None, None))
    if payment:
        result_pay = True#await check_payment(payment.id)
        if result_pay:
            id_user = call.from_user.id
            content = await after_pay(call, state)
            await add_payment_to_db(account=id_user, payment_key=payment.id, payment_date=payment.created_at)
            return content, start_keyboard()
        else:
            name_temp = 'error_pay'
            content = await create_answer_from_html(name_temp=name_temp)
            url_pay_keyboard = url_pay_keyboard_build(payment_url)
            return content, url_pay_keyboard
