# Программа, выводящая графическое изображение делимости чисел от 1 до n включительно.
# В каждой строке надо напечатать очередное число и столько символов +, сколько делителей у этого числа

n = int(input())

for i in range(1, n + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    print(i, '+' * count, sep='')