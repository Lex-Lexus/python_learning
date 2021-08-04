def to_dec(num_from, systema):
    stepen = 0
    total = 0
    for num in str(num_from)[::-1]:
        if num.lower() == 'a':
            num = 10
        elif num.lower() == 'b':
            num = 11
        elif num.lower() == 'c':
            num = 12
        elif num.lower() == 'd':
            num = 13
        elif num.lower() == 'e':
            num = 14
        elif num.lower() == 'f':
            num = 15
        total += int(num) * systema ** stepen
        stepen += 1
    return total

for i in range(2, 16):
    if to_dec(88, i) == to_dec(32, i) + to_dec(22, i) + to_dec(16, i) + to_dec(17, i):
        print(i)
        