# импорт библиотек
import random as rnd


# обьявление функций
def icosahedron(name, answers):
    while True:
        question = input('Задай вопрос: ')
        print(rnd.choice(answers))
        repeat = input('Хочеш ли ты задать еще вопрос?: ')
        if repeat == 'да' or repeat == 'Да':
            continue
        elif repeat == 'нет' or repeat == 'Нет':
            break
        else:
            print('Странно...')
            break


# инициализируем переменные
answers = ("Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно")

# вызываем функцию
print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('Напиши свое имя: ')
print('Привет', name)
icosahedron(name, answers)
print('Возвращайся если возникнут вопросы!')