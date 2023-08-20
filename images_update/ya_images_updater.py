import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
from typing import List
from loguru import logger

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
start_page = 0
query = 'it is wednesday my dude'

@logger.catch
def parse_yandex_images(query:str='it is wednesday my dude', start_page: int=0, limit: int=50) -> List[str] or False:
    """
    Парсинг страницы Яндекс.Картинок и получение ссылок на изображения.

    :param query: Запрос для поиска изображений (по умолчанию "it is wednesday my dude").
    :param start_page: Начальная страница для поиска (по умолчанию 0).
    :param limit: Максимальное количество изображений для получения (по умолчанию 50).
    :return: Список ссылок на изображения или False в случае ошибки.
    """
    try:
        image_urls = []
        while len(image_urls) < limit:
            url = f"https://yandex.ru/images/search?text={query}&p={start_page}"
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            images = soup.select('.serp-item__thumb')

            for image in images:
                image_url = image['src']
                if not image_url.startswith('https://'):
                    image_url = urljoin(url, image_url)
                image_urls.append(image_url)
                if len(image_urls) >= limit:
                    break
            start_page += 1
        return image_urls[:limit]
    except Exception as e:
        print(e)
        return False

@logger.catch
def download_images(image_urls) -> bool:
    """
    Загрузка изображений по ссылкам в каталог.

    :param image_urls: Список ссылок на изображения для загрузки.
    :return: True, если загрузка прошла успешно, иначе False.
    """
    try:
        current_dir = os.getcwd()  # Получаем текущий рабочий каталог
        folder_name = "images"  # Создаем папку загрузки в текущем рабочем каталоге
        save_folder = os.path.join(current_dir, folder_name)  # Путь папки для загрузок
        os.makedirs(save_folder, exist_ok=True)
        for i, url in enumerate(image_urls):
            response = requests.get(url)
            response.raise_for_status()
            file_path = os.path.join(save_folder, f"image_{i + 1}.jpg")
            with open(file_path, 'wb') as file:
                file.write(response.content)
        return True
    except Exception as e:
        print(e)
        return False

@logger.catch
def ya_updater(query=query, start_page=start_page, limit=50) -> bool:
    """
    Обновление картинок.

    :param query: Запрос для поиска изображений (по умолчанию "it is wednesday my dude").
    :param start_page: Начальная страница для поиска (по умолчанию 0).
    :param limit: Максимальное количество изображений для получения (по умолчанию 50).
    :return: True, если обновление прошло успешно, иначе False.
    """
    image_urls = parse_yandex_images(query=query, start_page=start_page, limit=limit) # Парсим ссылки на картинки с Яндекс.Картинок с ограничением в 50 картинок
    images = download_images(image_urls) # Загружаем картинки по ссылкам в папку
    if len(image_urls) > 0 and images == True:
        return True
    else: return False