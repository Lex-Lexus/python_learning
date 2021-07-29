# импорт библиотек
import random as rnd


# обьявление функций
def generate_password(length: int, chars: str):
    password = ''
    for _ in range(length):
        password += rnd.choice(chars)
    return password


# инициализируем переменные
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

# основной код
password_quantity = int(input('Количество паролей для генерации: '))
password_lenght = int(input('Длина одного пароля: '))
if input('Включать ли цифры 0123456789? д/н: ') == 'д':
    chars += digits
if input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? д/н: ') == 'д':
    chars += uppercase_letters
if input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? д/н: ') == 'д':
    chars += lowercase_letters
if input('Включать ли символы !#$%&*+-=?@^_? д/н: ') == 'д':
    chars += punctuation
if input('Исключать ли неоднозначные символы il1Lo0O? д/н: ') == 'д':
    for char in 'il1Lo0O':
        chars = chars.replace(char, '')

for _ in range(password_quantity):
    print(generate_password(password_lenght, chars))