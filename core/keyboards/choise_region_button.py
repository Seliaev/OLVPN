import json

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def choise_region_keyboard() -> InlineKeyboardMarkup:
    """
    Генерирует клавиатуру для выбора региона

    :return: InlineKeyboardMarkup - Объект InlineKeyboardMarkup, содержащий клавиатуру.
    """
    keyboard_builder = InlineKeyboardBuilder()
    region_buttons = create_region_button_from_json()
    if region_buttons:
        for button in region_buttons:
            keyboard_builder.button(text=button["name_ru"], callback_data=button["callback_data"])
    keyboard_builder.button(text='Назад', callback_data='back')
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()


def create_region_button_from_json() -> list:
    """
    Генерация названия и call_back данных для клавиатуры

    :return: list - список (call_back и текст)
    """
    config_file = 'core/api_s/outline/settings_api_outline.json'
    with open(config_file, 'r') as f:
        config = json.load(f)
    filtered_data = []
    for value in config.values():
        if value['is_active']:
            filtered_data.append({"callback_data": value["name_en"], "name_ru": value["name_ru"]})
    return filtered_data
