from aiogram.types import InlineKeyboardMarkup

from core.api_s.api_youkassa.youkassa_api import create_payment
from core.keyboards.url_pay_button import url_pay_keyboard_build
from core.utils.create_view import create_answer_from_html


async def build_pay(*args) -> (str, InlineKeyboardMarkup):
    """
    Запрос на создание платежа

    :param args:
                state: Объект CallbackQuery
                id_user: id пользователя (для создания комментария к платежу)
                amount: цена
                day_count: кол-во дней
                word_days: правильное склонение слова "день"
    :return: Текст ответа и клавиатура.
    """
    state, id_user, amount, day_count, word_days = args
    data = await state.get_data()
    name_temp = 'day'
    current = "руб"
    payment_url, payment = data.get('pay', (None, None))
    region_server = data.get('region_server', 'back')
    if payment_url is None or amount != int(payment.amount.value):
        payment_url, payment = await create_payment(amount_value=amount, count_day=day_count,
                                                    word_day=word_days, id_user=id_user)
    url_pay_keyboard = url_pay_keyboard_build(url_payment=payment_url, back_button=region_server)
    content = await create_answer_from_html(name_temp=name_temp, amount=amount, current=current,
                                            day_count=day_count, word_days=word_days)
    await state.update_data(pay=(payment_url, payment))
    await state.update_data(day_count=day_count)
    await state.update_data(word_days=word_days)
    return content, url_pay_keyboard
