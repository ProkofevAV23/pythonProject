# Дано натуральное число n(n>9). Программу, которая определяет его вторую (с начала) цифру

num = int(input())
while num > 9:
    second_digit = num % 10
    num = num // 10

print(second_digit)




