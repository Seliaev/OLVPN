from dotenv import load_dotenv
import os


# Загружает переменные среды из файла .env, если они доступны, или запрашивает их ввод у пользователя.
load_dotenv()

# Для бота tlg
api_key_tlg = os.getenv("API_KEY_TLG")
admin_tlg = os.getenv("ADMIN_TLG")

# Для сервера outline
# Перенесено в json файл /core/api_s/outline/settings_api_outline.json

# Для юкасса
client_id = os.getenv("YOUKASSA_ID")
secret_key = os.getenv("YOUKASSA_SECRET")

if not api_key_tlg:
    api_key_tlg = input("Введите токен бота телеграм: ")
    with open(".env", "a") as env_file:
        env_file.write(f"API_KEY_TLG={api_key_tlg}\n")

if not admin_tlg:
    admin_tlg = input("Введите id администратора бота: ")
    with open(".env", "a") as env_file:
        env_file.write(f"ADMIN_TLG={admin_tlg}\n")


if not client_id:
    client_id = input("Введите ID от ЮКасса: ")
    with open(".env", "a") as env_file:
        env_file.write(f"YOUKASSA_ID={client_id}\n")

if not secret_key:
    secret_key = input("Введите Secret Key от ЮКасса: ")
    with open(".env", "a") as env_file:
        env_file.write(f"YOUKASSA_SECRET={secret_key}\n")

