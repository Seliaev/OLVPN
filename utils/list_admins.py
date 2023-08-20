"""
Модуль работы с назначенными админами.

"""

from config_data.config import ADMIN_ID
from typing import List

def get_list_admin() -> List[str]:
    """
    Возвращение списка администраторов в виде строк.

    :return: Список администраторов в виде строк.
    """
    list_admins = list(map(str, ADMIN_ID.copy()))
    return list_admins

def add_new_admin(id) -> bool:
    """
    Добавление нового администратора.

    :param id: Идентификатор нового администратора.
    :return: True, если администратор успешно добавлен.
    """
    ADMIN_ID.append(id)
    return True


def del_admin(id) -> bool:
    """
    Удаление администратора по указанному идентификатору.

    :param id: Идентификатор администратора для удаления.
    :return: True, если администратор успешно удален, иначе False (если идентификатор не найден).
    """
    try:
        ADMIN_ID.remove(int(id))
        return True
    except ValueError:
        return False
