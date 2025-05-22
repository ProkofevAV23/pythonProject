# Программа, которая вычисляет сумму всех делителей введенного числа n

n = int(input())
div = 0

for i in range(1, n+1):
    if n % i == 0:
        div += i

print(div)
