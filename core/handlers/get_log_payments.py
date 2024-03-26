from aiogram.types import Message, FSInputFile
from core.settings import admin_tlg


async def command_get_log_pay(message: Message) -> None:
    """
    -- Админ-команда --
    Обработчик команды /get_log_pay.
    Отправляет в ответ файл с логами оплаты

    :param message: Message - Объект Message, полученный при вызове команды.
    """
    if message.from_user.id == int(admin_tlg):
        try:
            sending_log_file = FSInputFile(path='logs/payments/olvpnbot.log', filename="olvpnbot.log")
        except:
            await message.answer('Какая-то проблема с файлом логов')
        else:
            await message.answer_document(sending_log_file)
