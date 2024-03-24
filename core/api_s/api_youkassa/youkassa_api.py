import yookassa
from yookassa.domain.response import PaymentResponse

from core.settings import client_id, secret_key
from core.utils.format_iso_datetime import format_iso_datetime

yookassa.Configuration.account_id = client_id
yookassa.Configuration.secret_key = secret_key


async def create_payment(amount_value: int, count_day: int,
                         word_day: str, id_user: int) -> (str, yookassa.Payment):
    """
    Создание платежа

    :param amount_value: сумма платежа
    :param count_day: количество дней (для описания)
    :param word_day: склонение слова "день" (для описания)
    :param id_user: id пользователя телеграм (для описания)
    :return:
    """

    payment = yookassa.Payment.create(
        {
            "amount": {
                "value": amount_value,
                "currency": "RUB"
            },
            "confirmation": {
                "type": "redirect",
                "return_url": "https://t.me/olvpnbot"
            },
            "capture": True,
            "description": f"Ключ для аккаунта {id_user}\nна {count_day} {word_day}",
            "receipt": {
                "customer": {
                    "full_name": str(id_user),
                    "email": "email@email.ru",
                },
                "items": [
                    {
                        "description": f"Ключ для аккаунта {id_user}\nна {count_day} {word_day}",
                        "quantity": "1.00",
                        "amount": {
                            "value": amount_value,
                            "currency": "RUB"
                        },
                        "vat_code": "1",
                        "payment_mode": "full_payment"
                    },
                ]
            }
        }
    )

    url = payment.confirmation.confirmation_url
    return url, payment


async def check_payment(payment_id: PaymentResponse) -> bool:
    """
    Проверка платежа

    :param payment_id: id платежа для проверки
    :return: True в случае если платеж прошел, False в противном
    """
    payment = yookassa.Payment.find_one(payment_id)
    if payment.status == "succeeded":
        return True
    return False


async def get_user_payments(find_id: int) -> list:
    """
    Поиск платежей по id телеграм пользователя
    :return:
    """
    list_payments_from_youkassa = yookassa.Payment.list(params={'status': 'succeeded', 'limit': '50'})['items']
    list_payments = []
    for payment in list_payments_from_youkassa:
        if str(find_id) in payment['description'] and payment['status'] == 'succeeded':
            list_payments.append((payment['id'], payment['captured_at']))
    return await build_records_user_payments(list_payments)


async def build_records_user_payments(user_payments: list) -> list:
    """
    Создание списка, для шаблона к ответу на команду /findpay <id>

    :param user_payments: list - список из БД с записями об оплаченных покупках
    """
    str_user_payments = []
    for payment in user_payments:
        payment_key = payment[0]
        payment_time = format_iso_datetime(payment[1])
        str_user_payments.append(f"[*{payment_key[29:]}|{payment_time}]")
    return str_user_payments


if __name__ == "__main__":
    pass
