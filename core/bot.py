from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
from aiogram import Bot, Dispatcher, Router
import asyncio

from core.handlers.find_user_payments import command_findpay
from core.handlers.message_to_admin import send_admin_message
from core.settings import api_key_tlg
from core.api_s.outline.outline_api import OutlineManager
from core.handlers.handler_keyboard import build_and_edit_message
from core.handlers.start import command_start

router: Router = Router()
olm = OutlineManager()
BOT_TOKEN = api_key_tlg


async def start_bot():
    """Запуск бота"""
    bot: Bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
    dp: Dispatcher = Dispatcher()
    dp.include_router(router=router)
    dp.message.register(command_start, Command('start'))
    dp.message.register(command_findpay, Command('findpay'))
    dp.callback_query.register(build_and_edit_message)

    try:
        await send_admin_message(bot, "Бот был запущен.")
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await send_admin_message(bot, "Бот был остановлен.")
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start_bot())
