from aiogram.types import CallbackQuery
from datetime import datetime, timedelta

from core.api_s.outline.outline_api import OutlineManager
from core.sql.function_db_user_vpn.users_vpn import set_key_to_table_users, set_premium_status, set_date_to_table_users, \
    set_region_server


def get_future_date(add_day: int) -> str:
    """
    Добавление к текущей дате количество дней выбранной подписки

    :param add_day: кол-во дней подписки
    :return: Возврат даты окончания подписки в формате ДД.ММ.ГГГГ
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=add_day)
    return future_date.strftime('%d.%m.%Y - %H:%M')


async def get_ol_key_func(call: CallbackQuery, untill_date: str, region_server: str = 'nederland') -> str or bool:
    """
    Проверяет наличие ключа у пользователя
    Если ключа нет - создает.
    Устанавливает флажек премиум в True
    Устанавливает дату окончания премиума

    :param region_server: str - Регион раcположения сервера,
                                берется из ответа пользователя в choise_region() в get_key_handler.py
    :param untill_date: str - дата окончания подписки в формате ДД.ММ.ГГГГ - ЧЧ:ММ.
    :param call: CallbackQuery - Объект CallbackQuery.
    :return: Key - Объект Key, содержащий информацию о ключе пользователя или False
    """
    olm = OutlineManager(region_server)
    id_user = call.from_user.id
    key_user = olm.get_key_from_ol(id_user=str(id_user))
    if key_user is None:
        key_user = olm.create_key_from_ol(id_user=str(id_user))
    premium_user_db = await set_premium_status(account=id_user, value_premium=True)
    date_user_db = await set_date_to_table_users(account=id_user, value_date=untill_date)
    region_server_to_db = await set_region_server(account=id_user, value_region=region_server)
    if all((premium_user_db, date_user_db, region_server_to_db)):
        await set_key_to_table_users(account=id_user, value_key=key_user.access_url)
        return key_user
    return False
