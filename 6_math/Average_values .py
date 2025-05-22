# Программа, выводит 4 числа – среднее арифметическое, геометрическое, гармоническое и квадратичное

from math import sqrt, pow

a = float(input())
b = float(input())

p1 = ((a+b)/2)
p2 = sqrt(a*b)
p3 = ((2*(a*b))/(a+b))
p5 = pow(a, 2)
p6 = pow(b, 2)
p7 = p5+p6
p4 = sqrt(p7/2)

print(p1)
print(p2)
print(p3)
print(p4)



