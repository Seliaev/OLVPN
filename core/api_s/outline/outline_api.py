from core.settings import api_url, cert_sha256
from outline_vpn.outline_vpn import OutlineVPN, OutlineServerErrorException


class OutlineManager:
    """
    Класс для управления ключами в Outline VPN.

    Attributes:
    - client (OutlineVPN): Экземпляр класса OutlineVPN для взаимодействия с API Outline VPN.
    """

    def __init__(self):
        """
        Инициализация объекта OutlineManager.
        """
        self.client = OutlineVPN(api_url=api_url,
                                 cert_sha256=cert_sha256)

    def get_key_from_ol(self, id_user: str) -> str or None:
        """
        Получить ключ для указанного пользователя.

        Args:
        - id_user: str - Идентификатор пользователя.
        Returns:
        - str or None: Ключ пользователя или None, если ключ не найден.
        """
        try:
            key = self.client.get_key(id_user)
        except OutlineServerErrorException:
            key = None
        return key

    def create_key_from_ol(self, id_user: str) -> dict:
        """
        Создать новый ключ для пользователя.

        Args:
        - id_user: str - Идентификатор пользователя.

        Returns:
        - dict: Информация о созданном ключе.
        """
        return self.client.create_key(key_id=id_user, name=id_user)

    def delete_key_from_ol(self, id_user: str) -> bool:
        """
        Удалить ключ указанного пользователя.

        Args:
        - id_user: str - Идентификатор пользователя.

        Returns:
        - bool: True, если ключ успешно удален, False в противном случае.
        """
        key = self.get_key_from_ol(id_user=id_user)
        if key is None:
            return False
        return self.client.delete_key(key.key_id)

    # Для расширения функционала на будущее
    # def set_data_limit(self, id_user, limit):
    #     """Установка лимита по использованным данным"""
    #     key = self.get_key(id_user)
    #     if key is None:
    #         return None
    #     return self.client.add_data_limit(key.key_id, 1000 * 1000 * limit)
    #
    # def delete_data_limit(self, id_user):
    #     """Удаление лимита по использованным данным"""
    #     key = self.get_key(id_user)
    #     if key is None:
    #         return None
    #     return self.client.delete_data_limit(key.key_id)


if __name__ == "__main__":
    ol = OutlineManager()
