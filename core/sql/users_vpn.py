from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session
import uuid

from core.api_s.outline.outline_api import OutlineManager
from core.sql.base import Base, Users

DATABASE_URL = 'sqlite:///olvpnbot.db'
engine = create_engine(DATABASE_URL, echo=True)
Base.metadata.create_all(engine)


async def add_user_to_db(account: int, account_name: str) -> None:
    """
    Добавить нового пользователя в таблицу users_vpn

    :param account: int - id пользователя телеграм
    :param account_name: str - Имя пользователя телеграм
    :return: None
    """
    with Session(engine) as session:
        record_id = f"{account}_{uuid.uuid4()}"
        referal_link = f"id_{account}"

        new_record = Users(
            id=record_id,
            account=account,
            account_name=account_name,
            referal_link=referal_link
        )

        session.add(new_record)
        session.commit()


async def get_all_records_from_table_users() -> list[Users]:
    """
    Вывод всех записей таблицы users_vpn
    :return: list[Users] - Все записи из таблицы
    """
    session = Session(engine)
    try:
        result_all_records = session.query(Users).all()
        return result_all_records
    finally:
        session.close()


async def get_user_data_from_table_users(account: int) -> Users:
    """
    Находит и возвращает данные из таблицы users_vpn

    :param account:  int - id пользователя телеграм
    :return: Users - Данные из таблицы
    """
    with Session(engine) as session:
        try:
            user_data = session.query(Users).filter_by(account=account).one()
            return user_data
        except NoResultFound:
            return None


async def set_key_to_table_users(account: int, value_key: OutlineManager) -> bool:
    """
    Изменение ключа в таблице users_vpn

    :param account: int - Идентификатор записи
    :param value_key: str or None - Новое значение ключа outline vpn
    :return: bool - True в случае успеха, False в противном
    """
    with Session(engine) as session:
        try:
            user_record = session.query(Users).filter_by(account=account).one()
            if value_key != user_record.key:
                user_record.key = value_key
                session.commit()
            return True
        except NoResultFound:
            return False


async def set_premium_to_table_users(account: int, value_premium: bool) -> bool:
    """

    :param account: int - Данные из таблицы users_vpn
    :param value_premium: bool - Значение премиума
    :return: bool - True в случае успеха, False в противном
    """
    with Session(engine) as session:
        try:
            user_record = session.query(Users).filter_by(account=account).one()
            if value_premium != user_record.premium:
                user_record.premium = value_premium
                session.commit()
            return True
        except NoResultFound:
            return False


async def set_date_to_table_users(account: int, value_date: str) -> bool:
    """
    Установка даты до которого действует премиум

    :param account: int - Данные из таблицы
    :param value_date: str - Дата в формате ДД.ММ.ГГГГ - ЧЧ:ММ
    :return: bool - True в случае успеха, False в противном
    """
    with Session(engine) as session:
        try:
            user_record = session.query(Users).filter_by(account=account).one()
            if value_date:
                date = datetime.strptime(value_date, '%d.%m.%Y - %H:%M')
            elif value_date is None:
                date = datetime.strptime('01.01.2000 - 00:00', '%d.%m.%Y - %H:%M')
            if date != user_record.date:
                user_record.date = date
                session.commit()
            return True
        except NoResultFound:
            return False


async def set_promo_status(account: int, value_promo: bool) -> bool:
    """

    :param account: int - Данные из таблицы users_vpn
    :param value_promo: bool - Значение получен промо-ключ или нет
    :return: bool - True в случае успеха, False в противном
    """
    with Session(engine) as session:
        try:
            user_record = session.query(Users).filter_by(account=account).one()
            if value_promo != user_record.promo_key:
                user_record.promo_key = value_promo
                session.commit()
            return True
        except NoResultFound:
            return False


async def get_promo_status(account: int) -> bool:
    """
    Получение статуса промо для указанного пользователя

    :param account: int - Данные из таблицы users_vpn
    :return: bool - True если пользователь получал промо-ключ, False в противном случае
    """
    with Session(engine) as session:
        try:
            user_record = session.query(Users).filter_by(account=account).one()
            return user_record.promo_key
        except NoResultFound:
            return False
