import json


async def get_region_name_from_json(region: str) -> str or None:
    """
    Получение названия сервера на русском, в читаемом формате
    Из файла settings_api_outline.json

    :param region: str - Название региона в формате для бота
    :return: str - строка с названием региона сервера либо None если нет
    """
    config_file = 'core/api_s/outline/settings_api_outline.json'
    with open(config_file, 'r') as f:
        config = json.load(f)
    for key, value in config.items():
        if value['name_en'] == region:
            return value['name_ru']
    return None
