from telebot.types import ReplyKeyboardMarkup, KeyboardButton


list_settings_menu = ['Логи', 'Время отправки', 'Админы']

def keyboard_settings():
    # Клавиатура с основным меню админа
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for file_name in list_settings_menu:
        markup.add(file_name)
    markup.add(KeyboardButton("✅Закрыть меню"))
    return markup

