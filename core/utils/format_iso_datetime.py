from datetime import datetime


def format_iso_datetime(iso_datetime: str) -> str:
    """
    Преобразует строку с датой и временем в формате ISO 8601 в строку в удобном формате.

    :param iso_datetime: str Строка с датой и временем в формате ISO 8601.
    :return: Строка с датой и временем в формате "дд.мм.гг-чч:мм".
    """
    dt = datetime.fromisoformat(iso_datetime.replace("Z", "+00:00"))
    formatted_datetime = dt.strftime("%d.%m.%y - %H:%M")
    return formatted_datetime
