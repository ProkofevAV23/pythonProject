# Программа, определяющая евклидово расстояние между двумя точками, координаты которых заданы

from math import sqrt, pow

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

num1 = (x1-x2)
num2 = (y1-y2)
num3 = pow(num1, 2)
num4 = pow(num2, 2)
p = sqrt(num3+num4)

print(p)



