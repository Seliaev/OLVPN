from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from utils.get_error_from_log_json import get_all_file_log

list_files = get_all_file_log() # Получение списка названий всех файлов

def keyboard_with_files_log() -> ReplyKeyboardMarkup:
    """
    Генерация клавиатуры со списком файлов для выбора.

    :return: Экземпляр ReplyKeyboardMarkup с кнопками файлов и кнопкой для закрытия.
    """
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for file_name in list_files:
        markup.add(file_name)
    markup.add(KeyboardButton("✅Закрыть логи"))
    return markup

