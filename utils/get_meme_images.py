from os.path import join
from os import listdir
from random import choice

from config_data.config import MEME_IMAGES_FOLDER

LIST_FILES = []

def get_meme_image():
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

def get_random_path_meme():
    global LIST_FILES
    list_path_images = get_meme_image()
    if list_path_images == False or len(list_path_images) == 0 :
        return False
    else:
        path_meme = choice(list_path_images)
        index_path_meme = LIST_FILES.index(path_meme)
    return LIST_FILES.pop(index_path_meme)
