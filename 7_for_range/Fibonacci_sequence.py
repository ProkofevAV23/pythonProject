# Программа должна вывести члены последовательности Фибоначчи, отделенные символом пробела

n = int(input())
zero = 0
first = 1

if n >= 1:
    print(first, end=' ')

for i in range(1, n):
    num = zero + first
    zero = first
    first = num
    print(num, end=' ')
