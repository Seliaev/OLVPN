"""
Модуль получения списка всех файлов с картинками в images и случайный выбор одного из них.

"""

from os.path import join
from os import listdir
from random import choice
from typing import List
from config_data.config import MEME_IMAGES_FOLDER

LIST_FILES = [] # Список с файлами мем-картинок

def get_meme_image() -> List[str] or False:
    """
    Получение списка файлов с мемами.

    :return: Список путей к файлам с мемами (с расширениями .jpg или .png), либо False в случае ошибки.
    """
    global LIST_FILES
    try:
        if len(LIST_FILES) == 0:
            LIST_FILES =  [
                join(MEME_IMAGES_FOLDER, filename)
                for filename in listdir(MEME_IMAGES_FOLDER)
                if filename.endswith('.jpg') or filename.endswith('.png')
            ]
    except FileNotFoundError as e:
        print(e)
        return False
    return LIST_FILES


def get_random_path_meme() -> str or False:
    """
    Получение случайного пути к файлу с мемом.

    :return: Случайный путь к файлу с мемом (с расширением .jpg или .png), либо False, если нет доступных файлов.
    """
    global LIST_FILES
    list_path_images = get_meme_image()
    if list_path_images == False or len(list_path_images) == 0 :
        return False
    else:
        path_meme = choice(list_path_images)
        index_path_meme = LIST_FILES.index(path_meme)
    return LIST_FILES.pop(index_path_meme)
