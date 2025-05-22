# Программа выводит цифры натурального числа в столбик в обратном порядке.

num = int(input())
while num != 0:
    last_digit = num % 10
    print(last_digit)
    num = num // 10


