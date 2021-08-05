import random as rnd


def get_word(words):
    word = rnd.choice(words)
    word = word.upper()
    return word

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play(word):
    word_completion = ['_' for _ in word]       # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False                         # сигнальная метка
    guessed_letters = []                    # список уже названных букв
    guessed_words = []                      # список уже названных слов
    tries = 6                               # количество попыток
    print('Давайте играть в угадайку слов!')
    while tries > 0:
        print(display_hangman(tries))
        print(*word_completion)
        guess = input('Введите букву или слово: ').upper()
        if not guess.isalpha() or len(guess) == 0 or 1 < len(guess) < len(word):
            print('Можно вводить только букву или слово.')
            continue
        elif guess == word:
            print('Поздравляем, вы угадали слово! Вы победили!')
            return
        elif guess in word:
            for i in range(len(word)):
                if guess == word[i]:
                    word_completion[i] = guess
            if word_completion.count('_') == 0:
                print(*word_completion)
                print('Поздравляем, вы угадали слово! Вы победили!')
                return
            tries -= 1
        else:
            print(f'Ошибка, попробуйте еще раз. Осталось {tries} попыток.')
            tries -= 1


word_list = ['дом', 'лист', 'путь']

play(get_word(word_list))
