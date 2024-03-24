import asyncio
from datetime import datetime


async def check_time_subscribe(date: datetime) -> bool:
    """
    Проверка окончилась подписка или нет

    :param date: datetime - дата подписки
    :return: True в случае окончания, в противном False
    """
    if datetime.now() < date:
        return False
    return True


async def get_and_check_records(all_records: list) -> list:
    """
    Отправка на проверку подписки каждой записи из БД
    :param all_records: Все записи из БД списком
    :return: Записи на которых закончилась подписка
    """
    finish_subscribe = []
    try:
        for record in all_records:
            if await check_time_subscribe(record.date):
                finish_subscribe.append(record)
    finally:
        return finish_subscribe


async def finish_set_date_and_premium() -> None:
    """
    Изменение параметров (дата, премиум, ключ) в БД в случае окончания подписки
    Удаление ключа из Outline

    :return: None
    """
    from core.sql.users_vpn import get_all_records_from_table_users, set_premium_to_table_users, set_date_to_table_users, set_key_to_table_users
    from core.bot import olm
    all_records = await get_all_records_from_table_users()
    all_finish_records = await get_and_check_records(all_records)
    if all_finish_records:
        for record in all_finish_records:
            await set_key_to_table_users(account=record.account, value_key=None)
            await set_premium_to_table_users(account=record.account, value_premium=False)
            await set_date_to_table_users(account=record.account, value_date=None)
            olm.delete_key_from_ol(id_user=str(record.account))


async def main_check_subscribe():
    """
    Запуск цикла проверки БД на активную подписку
    :return:
    """
    while True:
        await finish_set_date_and_premium()
        await asyncio.sleep(3600) # Проверка раз в сутки


if __name__ == '__main__':
    asyncio.run(main_check_subscribe())
