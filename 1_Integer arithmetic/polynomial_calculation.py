# Программа, которая по введённым целым значениям a и b вычисляет значение следующего выражения:
# 3(a+b)^3 + 275b^2 − 127a − 41

c = input()
a = int(c)

d = input()
b = int(d)

print(3 * ((a + b) * (a + b) * (a + b)) + 275 * (b * b) - 127 * a - 41)

