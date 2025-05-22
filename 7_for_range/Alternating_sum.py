# Программа вычисления знакочередующейся суммы

n = int(input())
div = 0

for i in range(1, n + 1):
    div += i * (-1) ** (i + 1)

print(div)
