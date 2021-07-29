# импорт библиотек
import random

# обьявление функций
def main(num):
    while True:
        attempt = input('Введите число от 1 до 100: ')
        if attempt.isdigit():
            attempt = int(attempt)
            if attempt > num:
                print('Слишком много, попробуйте еще раз')
            elif attempt < num:
                print('Слишком мало, попробуйте еще раз')
            else:
                return 'Вы угадали, поздравляем!'
        else:
            print('Вы ввели не число.')
            continue


# считываем данные
num = random.randint(1, 100)

# вызываем функцию
print('Добро пожаловать в числовую угадайку')
print(main(num))