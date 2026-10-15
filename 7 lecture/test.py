from helpers.io import logger
from helpers.crypt import caesar_cipher


# Проверка логгера
logger("Старт программы")
logger("Тестовое сообщение")

# Проверка шифра Цезаря
original = "Привет, World!"
encrypted = caesar_cipher(original, shift=3)
decrypted = caesar_cipher(encrypted, shift=3, decrypt=True)

print("Оригинал:   ", original)
print("Зашифровано:", encrypted)
print("Расшифровано:", decrypted)