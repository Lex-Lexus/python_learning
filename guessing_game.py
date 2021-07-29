# импорт библиотек
import random

# обьявление функций
def main(num):
    while True:
        attempt = input('Введите число от 1 до 100: ')
        if is_valid(attempt):
            attempt = int(attempt)
            if attempt > num:
                print('Слишком много, попробуйте еще раз')
            elif attempt < num:
                print('Слишком мало, попробуйте еще раз')
            else:
                return 'Вы угадали, поздравляем!'
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue


def is_valid(attempt):
    if attempt.isdigit():
        return 1 <= int(attempt) <= 100
    else:
        return False


# считываем данные
num = random.randint(1, 100)

# вызываем функцию
print('Добро пожаловать в числовую угадайку')
print(main(num))