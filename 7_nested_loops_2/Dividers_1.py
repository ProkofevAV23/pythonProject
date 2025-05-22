# Программа, которая выводит два числа на одной строке, разделенных пробелом:
# число с максимальной суммой делителей и сумму его делителей.

a = int(input())
b = int(input())
max_sum = 0
max_x = 0

for x in range(a, b + 1):
    current_sum = 0
    for i in range(1, x + 1):
        if x % i == 0:
            current_sum += i
    if current_sum >= max_sum:
        max_sum = current_sum
        max_x = x

print(max_x, max_sum)