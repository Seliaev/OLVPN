from aiogram.types import Message

from core.keyboards.start_button import start_keyboard
from core.sql.users_vpn import add_user_to_db, get_user_data_from_table_users, set_key_to_table_users
from core.utils.create_view import create_answer_from_html


async def command_start(message: Message) -> None:
    """
    Обработчик команды /start.
    Проверяет наличие пользователя в БД и в Oitline менеджере
    В случае отсутствия в БД создает запись,
    Если есть ключ в Oitline добавляет в БД

    :param message: Message - Объект Message, полученный при вызове команды.
    """
    from core.bot import olm
    id_user = message.from_user.id
    check_user = await get_user_data_from_table_users(account=id_user)
    check_key = olm.get_key_from_ol(id_user=str(id_user))
    content = await create_answer_from_html(message.text)
    if check_user is None and check_key is None:
        name_user = f"{message.from_user.first_name}_{message.from_user.last_name}"
        await add_user_to_db(account=message.from_user.id, account_name=name_user)
    elif check_user is None and check_key is not None:
        name_user = f"{message.from_user.first_name}_{message.from_user.last_name}"
        await add_user_to_db(account=message.from_user.id, account_name=name_user)
        await set_key_to_table_users(account=id_user, value_key=check_key.access_url)
    await message.answer(text=content, reply_markup=start_keyboard())
