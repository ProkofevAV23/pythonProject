# Программа, вычисляющая значение тригонометрического выражения

from math import radians, cos, sin, tan, pow

a = float(input())

b = radians(a)
d = tan(b)
e = pow(d, 2)
c = sin(b)+cos(b)+e

print(c)



