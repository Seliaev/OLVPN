from aiogram.types import Message, FSInputFile
from core.settings import admin_tlg


async def command_get_db(message: Message) -> None:
    """
    -- Админ-команда --
    Обработчик команды /get_db.
    Отправляет в ответ файл с БД SQLite

    :param message: Message - Объект Message, полученный при вызове команды.
    """
    if message.from_user.id == int(admin_tlg):
        try:
            sending_db_file = FSInputFile(path='olvpnbot.db', filename="olvpnbot.db")
        except:
            await message.answer('Какая-то проблема с файлом БД')
        else:
            await message.answer_document(sending_db_file)
