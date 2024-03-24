from aiogram import Bot

from core.settings import admin_tlg


async def send_admin_message(bot: Bot, text: str) -> None:
    """
    Сообщение администратору о запуске и остановке бота
    :param bot: объект Bot, полученный при вызове команды.
    :param text: Текст сообщения для администратора
    :return: None
    """
    await bot.send_message(chat_id=admin_tlg, text=text)
