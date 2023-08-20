from database.init_db import DATABASE, db_lock


def check_subscribe(user_id) -> bool:
    """
    Проверка, подписан ли пользователь на еженедельную рассылку.

    :param user_id: Идентификатор пользователя.
    :return: True, если пользователь подписан, иначе False.
    """
    with db_lock:
        DATABASE.cursor.execute("SELECT user_id FROM subscriptions WHERE subscribed = 1")
        result = DATABASE.cursor.fetchall()
        subscribed_users = [row[0] for row in result]
    # Проверяем id пользователя в базе данных
    if user_id in subscribed_users:
        return True
    return False