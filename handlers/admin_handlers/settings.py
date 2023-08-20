"""
Модуль, содержащий обработчики сообщений для Telegram бота
Сообщения являются настройками бота, меню для админа.

"""

from telebot.types import Message
from loguru import logger
from config_data.config import ADMIN_ID
from loader import bot
from keyboards.reply.keyboard_settings import keyboard_settings
from telebot.types import ReplyKeyboardRemove
from keyboards.reply.keyboard_for_command_log_show import keyboard_with_files_log
from keyboards.reply.keyboard_settings_admins import keyboard_settings_admins
from utils.get_error_from_log_json import check_file
from utils.valid_time_format import is_valid_time
from main import schedule, send_zhabka
from utils.list_admins import get_list_admin, add_new_admin, del_admin


@logger.catch
@bot.message_handler(commands=["settings"])
def bot_settings(message: Message):
    '''
    Обработчик команды /settings.

    Если пользователь является администратором, отправляет сообщение с настройками(клавиатура keyboard_settings).

    :param message: Объект сообщения от Telegram бота.
    :return: None
    '''
    if message.chat.id in ADMIN_ID:
            bot.send_message(message.chat.id,"Выберите нужный пункт",reply_markup=keyboard_settings())

@logger.catch
@bot.message_handler(func=lambda message:True)
def all_messages(message):
    """
    Обработчик всех сообщений.

    Разбирает сообщения на различные действия в зависимости от текста сообщения.

    :param message: Объект сообщения от Telegram бота.
    :return: None
    """
    if message.text == "✅Закрыть меню":
        # Закрыть меню настроек
        markup = ReplyKeyboardRemove()
        bot.send_message(message.from_user.id,"Меню настроек закрыто",reply_markup=markup)


    elif message.text == "Логи":
        # Раздел меню с логами
        bot.send_message(message.chat.id,"Выберите файл, для просмотра логов",reply_markup=keyboard_with_files_log())
    elif message.text == "✅Закрыть логи":
        # Закрыть меню с логами
        markup = ReplyKeyboardRemove()
        bot.send_message(message.from_user.id,"Закрыт выбор файла логов",reply_markup=markup)


    elif message.text == "Админы":
        # Раздел меню с установкой новых админов
        bot.send_message(message.chat.id, "Выберете пункт меню", reply_markup=keyboard_settings_admins())
    elif message.text == "Текущие админы":
        # Вывод текущих админов
        text_answer = '\n'.join(get_list_admin())
        bot.send_message(message.chat.id, text_answer, reply_markup=keyboard_settings_admins())
    elif message.text == "Добавить администратора":
        # Добавление нового администратора
        bot.send_message(message.chat.id, "Введите id будущего администратора")
        bot.register_next_step_handler(message, process_add_new_admin)
    elif message.text == "Удалить администратора":
        # Удаление администратора
        bot.send_message(message.chat.id, "Введите id администратора для удаления")
        bot.register_next_step_handler(message, process_del_admin)
    elif message.text == "✅Закрыть меню с админами":
        # Закрыть меню с админами
        markup = ReplyKeyboardRemove()
        bot.send_message(message.from_user.id,"Закрыто меню с админами",reply_markup=markup)


    elif message.text == "Время отправки":
        # Редактирование времени рассылки
        bot.send_message(message.chat.id, "Введите время в формате 'часы:минуты' (от 00:00 до 23:59)")
        bot.register_next_step_handler(message, process_time_input)

    else:
        result = check_file(message.text)
        if result != 'Файл не найден.':
            answer_text = f'''<b>Выбран файл логов</b>: <i>{message.text}</i>
{result}
'''
            bot.send_message(message.chat.id, answer_text, parse_mode='HTML')


@logger.catch
def process_time_input(message):
    """
    Процесс установки нового времени рассылки и проверки на корректность этих данных:
    формат 'часы:минуты' (от 00:00 до 23:59)
    Если данные не верны, отправляется запрос на повторный ввод времени.

    :param message: Объект сообщения от Telegram бота.
    :return: None
    """
    new_time = message.text.strip()
    markup = ReplyKeyboardRemove()
    if is_valid_time(new_time):
        schedule.clear()
        schedule.every().wednesday.at(new_time).do(send_zhabka)
        bot.send_message(message.chat.id, f"Время выполнения задачи установлено на {new_time}", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, f"Некорректное время. Попробуйте еще раз ввести время в формате 'часы:минуты' (от 00:00 до 23:59)")
        bot.register_next_step_handler(message, process_time_input)


@logger.catch
def process_add_new_admin(message):
    """
    Процесс добавления нового администратора.

    Принимает id нового администратора из сообщения.
    Если id корректно(число), добавляет его в список администраторов.
    Если id не является числом, отправляет сообщение о некорректном вводе и просит ввести снова.

    :param message: Объект сообщения от Telegram бота.
    :return: None
    """
    id_new_admin = message.text
    if id_new_admin.isdigit() and add_new_admin(id_new_admin):
        bot.send_message(message.chat.id, f"Новый админ - {id_new_admin}")
    else:
        bot.send_message(message.chat.id, f"Не корректно был введет id\nДолжны быть цифры")
        bot.register_next_step_handler(message, process_add_new_admin)


@logger.catch
def process_del_admin(message):
    """
    Процесс удаления администратора.

    Принимает id администратора из сообщения.
    Если id корректно(число) и соответствует существующему администратору, удаляет его из списка администраторов.
    Если id не является числом или не соответствует существующему администратору,
    отправляет сообщение о некорректном вводе или отсутствии такого администратора, просит ввести снова.

    :param message: Объект сообщения от Telegram бота.
    :return: None
    """
    id_del_admin = message.text
    if id_del_admin.isdigit() and del_admin(id_del_admin):
        bot.send_message(message.chat.id, f"Удален админ - {id_del_admin}")
    else:
        bot.send_message(message.chat.id, f"Не корректно был введет id\nДолжны быть цифры\nЛибо данный id не является админом")
        bot.register_next_step_handler(message, process_del_admin)
