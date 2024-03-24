from os.path import join
from jinja2 import Template

ROOT_TEMPLATES = 'core/templates'  # Папка с шаблонами


def remove_left_slash(text: str):
    """Удаление префикса слеша для имени файла шаблона"""
    return text.removeprefix('/')


async def create_answer_from_html(name_temp: str, **kwargs) -> str:
    """
    Генерация ответа из шаблонов html

    :param name_temp: str - строка с названием шаблона
    :param kwargs: dict - параметры для передачи в шаблон
    :return str - строка с ответом из шаблона
    """
    page = remove_left_slash(name_temp)
    path = join(ROOT_TEMPLATES, f"{page}.html")
    try:
        with open(path, 'r') as f:
            template = Template(f.read())
            html_content = template.render(**kwargs)
    except:
        html_content = await create_answer_from_html("error", **kwargs)
    finally:
        return html_content
