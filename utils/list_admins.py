from config_data.config import ADMIN_ID
from typing import List

def get_list_admin() -> map[str]:
    # Возвращение списка с админами
    list_admins = map(str, ADMIN_ID.copy())
    return list_admins

def add_new_admin(id) -> bool:
    # Добавление нового админа
    ADMIN_ID.append(id)
    return True


def del_admin(id) -> bool:
    # Удаление админа
    try:
        ADMIN_ID.remove(int(id))
        return True
    except ValueError:
        return False
