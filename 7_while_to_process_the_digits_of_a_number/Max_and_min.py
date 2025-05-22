# Программа определяет максимальную и минимальную цифры числа и выводит текст

num = int(input())
maax = 0
miin = 9
while num != 0:
    last_digit = num % 10
    total = last_digit
    if total > maax:
        maax = total
    if total < miin:
        miin = total
    num = num // 10
print('Максимальная цифра равна', maax)
print('Минимальная цифра равна', miin)



