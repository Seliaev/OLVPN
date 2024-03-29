import json

from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup

from core.keyboards.time_button import time_keyboard
from core.utils.create_view import create_answer_from_html
from core.utils.get_region_name import get_region_name_from_json


async def region_handler(call: CallbackQuery, state: FSMContext) -> (str, InlineKeyboardMarkup):
    """
    Обработчик для выбора региона


    :param call: CallbackQuery - Объект CallbackQuery.
    :param state: FSMContext - Объект FSMContext.
    :return: Текст ответа и клавиатура.
    """
    id_user = call.from_user.id
    name_temp = 'choise_region'
    region_name = await get_region_name_from_json(region=call.data)
    await state.update_data(region_server=call.data)
    content = await create_answer_from_html(name_temp=name_temp, region_name=region_name)
    return content, await time_keyboard(id_user=id_user)

