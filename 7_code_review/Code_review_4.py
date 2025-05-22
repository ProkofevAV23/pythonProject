# На обработку поступает натуральное число.
# Программа выводит на экран максимальную цифру числа, кратную 3.
# Если в числе нет цифр, кратных 3, требуется на экран вывести «NO» (без кавычек).

n = int(input())
max_digit = -1
while n != 0:
    last_digit = n % 10
    if last_digit % 3 == 0 and last_digit > max_digit:
        max_digit = last_digit
    n = n // 10
if max_digit == -1:
    print('NO')
else:
    print(max_digit)



