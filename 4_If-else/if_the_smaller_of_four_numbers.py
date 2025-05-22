# Программа, которая определяет наименьшее из четырех чисел.

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

if num1>=num2:
    new12 = int(num2)
else: new12 = int(num1)

if num3>=num4:
    new34 = int(num4)
else: new34 = int (num3)

if new12>=new34:
    print(new34)
else: print(new12)


