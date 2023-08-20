from telebot.types import ReplyKeyboardMarkup, KeyboardButton


list_settings_menu = ['Логи', 'Время отправки', 'Админы']

def keyboard_settings() -> ReplyKeyboardMarkup:
    """
    Генерация клавиатуры с основным меню настроек админа.

    :return: Экземпляр ReplyKeyboardMarkup с кнопками меню настроек и кнопкой для закрытия.
    """
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for file_name in list_settings_menu:
        markup.add(file_name)
    markup.add(KeyboardButton("✅Закрыть меню"))
    return markup

