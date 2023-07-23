from utils.schedule_checker import schedule_checker, schedule
from utils.send_zhabka import send_zhabka
from loader import bot
import handlers  # noqa
from utils.set_commands import set_commands
from telebot.custom_filters import StateFilter
from threading import Thread


if __name__ == "__main__":
    bot.add_custom_filter(StateFilter(bot))
    set_commands(bot)    # Отправка команд боту
    schedule.every().sunday.at("00:00").do(send_zhabka)    # Установка времени для отправки рассылки и отсылки к нужной функции
    Thread(target=schedule_checker).start()    # Запуск потока для проверки времени расписания
    bot.infinity_polling()    # Запуск бота
