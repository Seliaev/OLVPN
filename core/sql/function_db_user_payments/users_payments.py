from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from core.sql.base import Base, UserPay
from core.sql.function_db_user_vpn.users_vpn import get_user_data_from_table_users, add_user_to_db
from core.utils.format_iso_datetime import format_iso_datetime

DATABASE_URL = 'sqlite:///olvpnbot.db'
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)


async def add_payment_to_db(account: int, payment_key: str, payment_date: str) -> None:
    """
    Добавить новый платеж пользователя в таблицу users_payments

    :param account: int - id пользователя телеграм
    :param payment_key: str - ключ платежа
    :param payment_date: str - дата и время платежа
    :return: None
    """
    with Session() as session:
        existing_record = session.query(UserPay).filter(UserPay.account_id == account).first()
        payment_date = format_iso_datetime(iso_datetime=payment_date)
        if existing_record:
            existing_record.paykey += f"\n[{payment_key}|{payment_date}]"
        else:
            record_from_table_user = await get_user_data_from_table_users(account=account)
            if record_from_table_user is None:
                await add_user_to_db(account=account, account_name=account)
                record_from_table_user = await get_user_data_from_table_users(account=account)
            record_id = record_from_table_user.id
            new_record = UserPay(
                id=record_id,
                account_id=account,
                paykey=f"[{payment_key}|{payment_date}]",
                time_added=datetime.now()
            )
            session.add(new_record)
        session.commit()


async def get_all_accounts_from_db() -> list:
    """
    Получить список всех account_id из таблицы UserPay
    :return: list - список всех account_id
    """
    with Session() as session:
        all_accounts = session.query(UserPay.account_id).distinct().all()
        return [str(account[0]) for account in all_accounts]