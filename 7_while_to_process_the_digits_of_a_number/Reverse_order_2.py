# Программа меняет порядок цифр числа на обратный

num = int(input())
while num != 0:
    last_digit = num % 10
    num = num // 10
    print(last_digit, end='')


