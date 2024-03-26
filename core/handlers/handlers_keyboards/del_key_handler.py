from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup

from core.keyboards.accept_del_button import accept_del_keyboard
from core.keyboards.start_button import start_keyboard
from core.sql.users_vpn import set_key_to_table_users, set_premium_status, set_date_to_table_users, \
    get_key_from_table_users
from core.utils.create_view import create_answer_from_html
from main import logger_payments


async def ask_del_key(call: CallbackQuery, state: FSMContext) -> (str, InlineKeyboardMarkup):
    """
    Обработчик для удаления ключа.

    :param call: CallbackQuery - Объект CallbackQuery.
    :param state: FSMContext - Объект FSMContext.
    :return: Текст ответа и клавиатура.
    """
    from core.bot import olm
    id_user = call.from_user.id
    key_user_db = await get_key_from_table_users(account=id_user)
    key_user = olm.get_key_from_ol(id_user=str(id_user))
    name_temp = call.data
    if key_user and key_user_db:
        result, return_keyboard = 'Подтверждаете удаление ключа?', accept_del_keyboard()
    else:
        result, return_keyboard = 'Возможно произошла ошибка, либо ключа у вас не существует.', start_keyboard()
    content = await create_answer_from_html(name_temp=name_temp, result=result)
    return content, return_keyboard


async def del_key(call: CallbackQuery, state: FSMContext) -> (str, InlineKeyboardMarkup):
    """
    Обработчик для удаления ключа.

    :param call: CallbackQuery - Объект CallbackQuery.
    :param state: FSMContext - Объект FSMContext.
    :return: Текст ответа и клавиатура.
    """
    from core.bot import olm
    id_user = call.from_user.id
    key_user_db = await set_key_to_table_users(account=id_user, value_key=None)
    premium_user_db = await set_premium_status(account=id_user, value_premium=False)
    date_user_db = await set_date_to_table_users(account=id_user, value_date=None)
    key_user = olm.delete_key_from_ol(id_user=str(id_user))
    name_temp = call.data
    if key_user and key_user_db and premium_user_db and date_user_db:
        logger_payments.log('info', f'{id_user} удалил свой ключ')
        result = 'удален.'
    else:
        result = 'не удален.\nВозможно произошла ошибка, либо ключа у вас не существует.'
    content = await create_answer_from_html(name_temp=name_temp, result=result)
    return content, start_keyboard()
