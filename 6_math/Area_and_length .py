# Программа, определяющая определяющую площадь круга и длину окружности по заданному радиусу R

from math import pow, pi

R = float(input())

num1 = pow(R, 2)
num2 = (pi*num1)
num3 = (2*pi*R)

print(num2)
print(num3)



