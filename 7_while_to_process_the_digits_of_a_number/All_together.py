# Дано натуральное число. Программу вычисляет:
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.

num = int(input())
total = 0
count = 0
product = 1
last_digit_1 = num % 10
while num != 0:
    last_digit = num % 10
    total = last_digit + total
    count = count + 1
    product = product * last_digit
    first_digit = last_digit
    num = num // 10
arithmetic_mean = total/count
sum_first_and_last = first_digit + last_digit_1

print(total)
print(count)
print(product)
print(arithmetic_mean)
print(first_digit)
print(sum_first_and_last)




