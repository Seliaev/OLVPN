from dotenv import load_dotenv
import os


# Загружает переменные среды из файла .env, если они доступны, или запрашивает их ввод у пользователя.
load_dotenv()

# Для бота tlg
api_key_tlg = os.getenv("API_KEY_TLG")
admin_tlg = os.getenv("ADMIN_TLG")
# Для сервера outline
api_url = os.getenv("API_URL")
cert_sha256 = os.getenv("CERT_SHA256")
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

if not api_url:
    api_url = input("Введите api url outline сервера: ")
    with open(".env", "a") as env_file:
        env_file.write(f"API_URL={api_url}\n")

if not cert_sha256:
    cert_sha256 = input("Введите сертификат sha256 outline сервера: ")
    with open(".env", "a") as env_file:
       env_file.write(f"CERT_SHA256={cert_sha256}\n")

if not client_id:
    client_id = input("Введите ID от ЮКасса: ")
    with open(".env", "a") as env_file:
        env_file.write(f"YOUKASSA_ID={client_id}\n")

if not secret_key:
    secret_key = input("Введите Secret Key от ЮКасса: ")
    with open(".env", "a") as env_file:
        env_file.write(f"YOUKASSA_SECRET={secret_key}\n")

