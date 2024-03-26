from typing import Callable, Tuple

from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup

from core.handlers.handlers_keyboards.after_pay_handler import pay_check_key
from core.handlers.handlers_keyboards.back_key_handler import back_key
from core.handlers.handlers_keyboards.get_key_handler import get_key, day_key, week_key, month_key, my_key
from core.handlers.handlers_keyboards.del_key_handler import del_key, ask_del_key
from core.handlers.handlers_keyboards.get_link_to_app_handler import get_link_to_app
from core.handlers.handlers_keyboards.get_promo_handler import get_promo
from core.utils.throttle import throttle


@throttle(seconds=0.2)
async def build_and_edit_message(call: CallbackQuery, state: FSMContext):
    """
    Обработчик для вывода меню и редактирования сообщения.

    :param call: CallbackQuery - Объект CallbackQuery.
    :param state: FSMContext - Объект FSMContext.
    """
    await call.answer()
    data = call.data
    text, reply_markup = await switch_menu(data, call, state)
    if text != call.message.text:
        await call.message.edit_text(text=text, reply_markup=reply_markup)


async def switch_menu(case_number: str, call: CallbackQuery, state: FSMContext) -> Tuple[str, InlineKeyboardMarkup]:
    """
    Выбор обработчика, основываясь на callback-ключе.

    :param case_number: str - Ключ для определения необходимого обработчика.
    :param call: CallbackQuery - Объект CallbackQuery.
    :param state: FSMContext - Объект FSMContext.
    :return: Результат работы соответствующего обработчика.
    """
    switch_dict = {
        'get_key': get_key,
        'get_link_to_app': get_link_to_app,
        'del_key': del_key,
        'ask_del_key': ask_del_key,
        'day': day_key,
        'week': week_key,
        'month': month_key,
        'back': back_key,
        'pay_check': pay_check_key,
        'my_key': my_key,
        'promo': get_promo,
    }

    default_handler: Callable[[CallbackQuery, FSMContext],
                     Tuple[str, InlineKeyboardMarkup]] = \
                    lambda call, state: ("", InlineKeyboardMarkup())

    handler: Callable[[CallbackQuery, FSMContext],
             Tuple[str, InlineKeyboardMarkup]] = (
            switch_dict.get(case_number, default_handler))

    return await handler(call, state)
