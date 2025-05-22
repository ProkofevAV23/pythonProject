# Программа определяет, является ли последовательность его цифр при просмотре справа налево упорядоченной по неубыванию.
# Программа должна вывести «YES» (без кавычек),
# если последовательность его цифр при просмотре справа налево является упорядоченной по неубыванию,
# или «NO» (без кавычек) в противном случае.

num = int(input())
last_digit = num % 10
ordered = True

while num != 0:
    current_digit = num % 10
    if current_digit < last_digit:
        ordered = False
    last_digit = current_digit
    num //= 10

if ordered:
    print("YES")
else:
    print("NO")




