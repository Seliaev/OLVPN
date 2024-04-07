from aiogram.types import Message

from core.settings import admin_tlg
from core.sql.function_db_user_vpn.users_vpn import set_promo_status


async def command_promo(message: Message) -> None:
    """
    -- Админ-команда --
    Обработчик команды /promo <id>.
    Дает пользователю возможность получить промо - по id

    :param message: Message - Объект Message, полученный при вызове команды.
    """
    if message.from_user.id == int(admin_tlg):
        data = message.text.split(' ')
        if len(data) == 2:
            name_temp, id_find_user = data
            result_set_promo = await set_promo_status(account=id_find_user, value_promo=False)
            content = f"Пользователю {id_find_user} {'удалось' if result_set_promo else 'не удалось'} выдать промо"
            await message.answer(text=content)



