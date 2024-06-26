from aiogram.types import Message

from core.api_s.api_youkassa.youkassa_api import get_user_payments
from core.settings import admin_tlg
from core.sql.function_db_user_payments.users_payments import get_all_accounts_from_db
from core.utils.create_view import create_answer_from_html


async def command_findpay(message: Message) -> None:
    """
    -- Админ-команда --
    Обработчик команды /findpay <id>.
    Проверяет наличие записей о покупках пользователя по id
    Выдает их если есть.

    :param message: Message - Объект Message, полученный при вызове команды.
    """
    if message.from_user.id == int(admin_tlg):
        data = message.text.split(' ')
        if len(data) == 2:
            name_temp, id_find_user = data
            user_payments = await get_user_payments(find_id=int(id_find_user))
            content = await create_answer_from_html(name_temp=name_temp, id_find_user=id_find_user, payments=user_payments)
            await message.answer(text=content)
        elif len(data) == 1:
            name_temp = data[0]
            users_who_paid = await get_all_accounts_from_db()
            content = await create_answer_from_html(name_temp=name_temp, id_find_user='[ALL]', payments=users_who_paid)
            await message.answer(text=content)


