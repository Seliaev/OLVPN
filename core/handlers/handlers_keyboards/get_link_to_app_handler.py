from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup

from core.keyboards.url_app_button import url_app_keyboard
from core.utils.create_view import create_answer_from_html


async def get_link_to_app(call: CallbackQuery, state: FSMContext) -> (str, InlineKeyboardMarkup):
    """
    Обработчик для получения ссылки на приложение.
    Ссылка на страницу загрузки приложений с официального сайта Outline

    :param call: CallbackQuery - Объект CallbackQuery.
    :param state: FSMContext - Объект FSMContext.
    :return: Текст ответа и клавиатура.
    """
    name_temp = call.data
    content = await create_answer_from_html(name_temp)
    return content, url_app_keyboard()
