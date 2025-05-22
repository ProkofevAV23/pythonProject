# Программа должна вывести текст «YES» (без кавычек), если все числа чётные, или «NO» (без кавычек) в противном случае

all_even = True

for i in range(1, 11):
    n = int(input())
    if n % 2 != 0:
        all_even = False

if all_even:
    print('YES')
else:
    print('NO')


