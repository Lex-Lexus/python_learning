# объявление функций
def crypt(alphabet, rotate, text):
    text_new = ''
    for i in range(len(text)):
        if text[i] in alphabet[0]:
            index_old_in_alphabet = alphabet[0].index(text[i])
            index_new_in_alphabet = index_old_in_alphabet + rotate
            if index_new_in_alphabet >= len(alphabet[0]):
                index_new_in_alphabet -= len(alphabet[0])
            text_new += alphabet[0][index_new_in_alphabet]
        elif text[i] in alphabet[1]:
            index_old_in_alphabet = alphabet[1].index(text[i])
            index_new_in_alphabet = index_old_in_alphabet + rotate
            if index_new_in_alphabet >= len(alphabet[0]):
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
alphabet = [[chr(i) for i in range(ord('a'), ord('z') + 1)], [chr(i) for i in range(ord('A'), ord('Z') + 1)]]
text_new = []

# основной код
print('Вас приветствует шифратор и дешифратор Цезаря')
print('')

print('Что будем делать?')
type_of_work = input('1 - Зашифровать?, 0 - Расшифровать?: ')
text = input('Введите текст: ').split()
for word in text:
    word_len = 0
    for char in word:
        if char.isalpha():
            word_len += 1
    if type_of_work == '1':
        text_new.append(crypt(alphabet, word_len, word))
    elif type_of_work == '0':
        text_new.append(decrypt(alphabet, word_len, word))
print(*text_new)
