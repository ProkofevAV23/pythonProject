# Программа определяет, состоит ли указанное число из одинаковых цифр.
# Программа должна вывести «YES» (без кавычек), если число состоит из одинаковых цифр,
# или «NO» (без кавычек) в противном случае.

num = int(input())
last_digit = num % 10
all_same = True

while num != 0:
    current_digit = num % 10
    if current_digit != last_digit:
        all_same = False
    num //= 10

if all_same:
    print("YES")
else:
    print("NO")




