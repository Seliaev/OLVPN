import json

from outline_vpn.outline_vpn import OutlineVPN, OutlineServerErrorException


def get_name_all_active_server_ol() -> list:
    """
    Получение всех активных серверов
    Данные для сервера берутся из settings_api_outline.json

    :return: list - name_en всех активных серверов
    """
    config_file = 'core/api_s/outline/settings_api_outline.json'
    active_servers = []
    with open(config_file, 'r') as f:
        config = json.load(f)
    for value in config.values():
        if value['is_active']:
            active_servers.append(value['name_en'])
        return active_servers


class OutlineManager:
    """
    Класс для управления ключами в Outline VPN.

    Attributes:
    - client (OutlineVPN): Экземпляр класса OutlineVPN для взаимодействия с API Outline VPN.
    """

    def __init__(self, region_server: str = 'nederland'):
        """
        Инициализация объекта OutlineManager

        Args:
        - region_server: str - Регион сервера для инициализации клиента
        """

        self.region_server = region_server
        self._client = self.__client_init()

    def __client_init(self) -> OutlineVPN:
        """
        Инициализация клиента
        Данные для сервера берутся из settings_api_outline.json

        :return: OutlineVPN - Объект OutlineVPN
        """
        config_file = 'core/api_s/outline/settings_api_outline.json'
        with open(config_file, 'r') as f:
            config = json.load(f)
        data_server = config[self.region_server]
        api_url = data_server['api_url']
        cert_sha256 = data_server['cert_sha256']
        return OutlineVPN(api_url=api_url,
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
            key = self._client.get_key(id_user)
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
        return self._client.create_key(key_id=id_user, name=id_user)

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
        return self._client.delete_key(key.key_id)


if __name__ == "__main__":
    ol = OutlineManager()
