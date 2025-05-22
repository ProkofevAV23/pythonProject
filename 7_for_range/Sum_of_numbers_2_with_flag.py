# Программа, которая подсчитывает сумму тех чисел от 1 до n (включительно), квадрат которых оканчивается на 2, 5 или 8.

n = int(input())
total = 0
condition_met = False  # Флаг для отслеживания выполнения условия

for i in range(1, n + 1):
    if i ** 2 % 10 == 2 or i ** 2 % 10 == 5 or i ** 2 % 10 == 8:
        total += i
        condition_met = True  # Условие выполнено хотя бы один раз

if not condition_met:
    print(0)
else:
    print(total)
