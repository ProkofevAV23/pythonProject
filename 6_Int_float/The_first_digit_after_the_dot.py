# Дано положительное действительное число. Вывести его первую цифру после десятичной точки.

number1 = float(input())
number2 = int(number1 * 10)

digit_after_dot = (number2 % 10)

print(digit_after_dot)

