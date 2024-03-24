from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup

from core.keyboards.start_button import start_keyboard
from core.sql.users_vpn import get_promo_status, set_promo_status
from core.utils.create_view import create_answer_from_html
from core.utils.get_key_utils import get_future_date, get_ol_key_func


async def get_promo(call: CallbackQuery, state: FSMContext) -> (str, InlineKeyboardMarkup):
    """
    Обработчик для получения промо-ключа.
    Отправка ключа, если пользователь еще не получал промо-ключ

    :param call: CallbackQuery - Объект CallbackQuery.
    :param state: FSMContext - Объект FSMContext.
    :return: Текст ответа и клавиатура.
    """
    id_user = call.from_user.id
    content = f"<b>Вы уже получали промо-ключ</b>"
    name_temp = call.data
    promo_status = await get_promo_status(account=id_user)
    if not promo_status:
        await set_promo_status(account=id_user, value_promo=True)
        add_day = 1
        untill_date = get_future_date(add_day=add_day)
        key_user = await get_ol_key_func(call=call, untill_date=untill_date)
        content = await create_answer_from_html(name_temp=name_temp,
                                                key_user=key_user.access_url, untill_date=untill_date)
    return content, start_keyboard()
