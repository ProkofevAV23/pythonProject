# На вход программе подаётся последовательность целых чисел, каждое число на отдельной строке.
# Признаком окончания последовательности является любое отрицательное число,
# при этом в саму последовательность оно не входит.
# Программа выводит сумму всех членов данной последовательности.

num = int(input())
cnt = 0

while num >= 0:
    cnt += num
    num = int(input())
print(cnt)
