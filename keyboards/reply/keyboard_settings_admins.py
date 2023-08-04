from telebot.types import ReplyKeyboardMarkup, KeyboardButton


list_settings_admins_menu = ['Текущие админы', 'Добавить администратора', 'Удалить администратора']

def keyboard_settings_admins():
    # Клавиатура для управления администраторами
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for file_name in list_settings_admins_menu:
        markup.add(file_name)
    markup.add(KeyboardButton("✅Закрыть меню с админами"))
    return markup