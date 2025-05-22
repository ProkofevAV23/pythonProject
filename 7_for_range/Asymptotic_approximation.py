# Программа, которая вычисляет значение выражения

from math import log

n = int(input())
num = 0

for i in range(1, n):
    num = num + (1/(i+1))
num1 = num + 1 - log(n)
print(num1)
