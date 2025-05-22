# Программа, которая считывает три числа и подсчитывает сумму только положительных чисел.

num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 >= 0:
    num4 = int(num1)
else: num4 = 0

if num2 >= 0:
    num5 = int(num2)
else: num5 = 0

if num3 >= 0:
    num6 = int(num3)
else: num6 = 0

if num4+num5+num6 == 0:
     print(0)
else: print(num4+num5+num6)


