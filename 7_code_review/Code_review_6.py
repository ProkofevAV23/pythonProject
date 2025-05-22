# На обработку поступает натуральное число.
# Программа выводит на экран произведение цифр введённого числа

n = int(input())
product = 1
while n != 0:
    digit = n % 10
    product = product * digit
    n //= 10
print(product)



