# объявление функций
def crypt(alphabet, rotate, text):
    text_new = ''
    for i in range(len(text)):
        if text[i] in alphabet[0]:
            index_old_in_alphabet = alphabet[0].index(text[i])
            index_new_in_alphabet = index_old_in_alphabet + rotate
            if index_new_in_alphabet > len(alphabet[0]):
                index_new_in_alphabet -= len(alphabet[0])
            text_new += alphabet[0][index_new_in_alphabet]
        elif text[i] in alphabet[1]:
            index_old_in_alphabet = alphabet[1].index(text[i])
            index_new_in_alphabet = index_old_in_alphabet + rotate
            if index_new_in_alphabet > len(alphabet[0]):
                index_new_in_alphabet -= len(alphabet[0])
            text_new += alphabet[1][index_new_in_alphabet]
        else:
            text_new += text[i]
    return text_new

def decrypt(alphabet, rotate, text):
    text_new = ''
    for i in range(len(text)):
        if text[i] in alphabet[0]:
            index_old_in_alphabet = alphabet[0].index(text[i])
            index_new_in_alphabet = index_old_in_alphabet - rotate
            if index_new_in_alphabet < 0:
                index_new_in_alphabet += len(alphabet[0])
            text_new += alphabet[0][index_new_in_alphabet]
        elif text[i] in alphabet[1]:
            index_old_in_alphabet = alphabet[1].index(text[i])
            index_new_in_alphabet = index_old_in_alphabet - rotate
            if index_new_in_alphabet < 0:
                index_new_in_alphabet += len(alphabet[0])
            text_new += alphabet[1][index_new_in_alphabet]
        else:
            text_new += text[i]
    return text_new


# инициализация переменных
alphabet_ru_en = [[[chr(i) for i in range(ord('а'), ord('я') + 1)], [chr(i) for i in range(ord('А'), ord('Я') + 1)]],
                  [[chr(i) for i in range(ord('a'), ord('z') + 1)], [chr(i) for i in range(ord('A'), ord('Z') + 1)]]]


# основной код
print('Вас приветствует шифратор и дешифратор Цезаря')
print('Что будем делать?')
type_of_work = input('1 - Зашифровать?, 0 - Расшифровать?: ')
print('Язык шифрования?')
alphabet = alphabet_ru_en[int(input('0 - Русский?, 1 - Английский?: '))]
rotate = int(input(f'Шаг сдвига от 0 до {len(alphabet[0])}: '))
text = input('Введите текст: ')
if type_of_work == '1':
    print(crypt(alphabet, rotate, text))
elif type_of_work == '0':
    print(decrypt(alphabet, rotate, text))
