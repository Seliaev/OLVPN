"""
Модуль составления тела сообщения из файла с логами и вывод в ответном сообщении

"""

import os
import json
import html
from datetime import datetime

def get_all_file_log() -> list:
    """
    Получение списка названий всех файлов логов.

    :return: Список названий файлов логов.
    """
    files_name_list = []
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, "logs")
    for i_name_file in os.listdir(file_path):
        if i_name_file.endswith(".json"):
            files_name_list.append(i_name_file)
    return files_name_list


def check_file(filename: str) -> str:
    """
    Проверка и анализ содержимого файла лога JSON.

    :param filename: Название файла лога.
    :return: Строка с данными об ошибках из файла лога.
    """

    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, "logs", filename)
    answer = ''
    try:
        with open(file_path, "r") as file:
            for line in file:
                try:
                    data = json.loads(line)
                    # Извлеките необходимые данные
                    time_str = data['record']['time']['repr']
                    level = data['record']['level']['name']
                    error_type = data['record']['exception']['type']
                    error_message = data['record']['exception']['value']
                    file_name = data['record']['file']['name']
                    function = data['record']['function']
                    line = data['record']['line']

                    time_obj = datetime.fromisoformat(time_str.replace("Z", "+00:00"))
                    formatted_time = time_obj.strftime("%d.%m.%Y %H:%M")
                    escaped_error_message = error_message.replace('(', '\(').replace(')', '\)')
                    answer += f"""<b>Время</b>: <i>{formatted_time}</i>
<b>Уровень сообщения</b>: <i>{level}</i>
<b>Тип ошибки</b>: <i>{error_type}</i>
<b>Сообщение об ошибке</b>: <i>{escaped_error_message}</i>
<b>Название файла ошибки</b>: <i>{file_name}</i>
<b>Функция</b>: <i>{html.escape(function)}</i>
<b>Линия</b>: <i>{line}</i>

"""
                except json.JSONDecodeError as e:
                    return f"Ошибка декодирования JSON: {e}"
        return answer
    except FileNotFoundError:
        return "Файл не найден."
    except json.JSONDecodeError as e:
        return f"Ошибка декодирования JSON: {e}"


