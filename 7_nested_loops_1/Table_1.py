# Программа, которая печатает таблицу размером n×3, состоящую из данного числа

n = int(input())

for i in range(n):
    for j in range(3):
        print(n, end=' ')
    print()
