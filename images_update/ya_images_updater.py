import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
from .ya_config import headers, query, start_page
from loguru import logger


@logger.catch
def parse_yandex_images(query:str='it is wednesday my dude', start_page: int=0, limit: int=50):
    # Парсинг страницы Яндекс.Картинок и получение ссылок на изображения
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
def download_images(image_urls):
    # Загрузка изображений по ссылкам в каталог
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
def ya_updater(query=query, start_page=start_page, limit=50):
    # Обновление картинок
    image_urls = parse_yandex_images(query=query, start_page=start_page, limit=limit) # Парсим ссылки на картинки с Яндекс.Картинок с ограничением в 50 картинок
    images = download_images(image_urls) # Загружаем картинки по ссылкам в папку
    if len(image_urls) > 0 and images == True:
        return True
    else: return False