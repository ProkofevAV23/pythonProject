# Программа, которая назовёт число красивым, если оно является четырёхзначным и делится нацело на  7 или на 17
# Программа должна вывести «YES» (без кавычек), если число является красивым, или «NO» (без кавычек) в противном случае.

x = int(input())

if 1000 <= x < 10000 and (x % 7 == 0 or x % 17 == 0):
    print('YES')
else: print ('NO')


