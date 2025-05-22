# Дано трехзначное число abc, в котором все цифры различны.
# Программа, которая выводит шесть чисел, образованных при перестановке цифр заданного числа.

num = int(input())
digit3 = num % 10
digit2 = (num // 10) % 10
digit1 = num // 100

print(digit1, digit2, digit3, sep='')
print(digit1, digit3, digit2, sep='')
print(digit2, digit1, digit3, sep='')
print(digit2, digit3, digit1, sep='')
print(digit3, digit1, digit2, sep='')
print(digit3, digit2, digit1, sep='')
