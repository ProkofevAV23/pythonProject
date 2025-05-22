# Программа, которая печатает численный треугольник с высотой, равной n

num = 1
n = int(input())

for i in range(1, n+1):
    for j in range(1, i+1):
        print(num, end=' ')
        num += 1
    print()

