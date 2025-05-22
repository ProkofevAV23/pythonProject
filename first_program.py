# Программа для нахождения цифр четырёхзначного числа.

# num = int(input())
# digit4 = num % 10
# digit3 = (num // 10) % 10
# digit2 = (num // 100) % 10
# digit1 = num // 1000
#
# if digit1 + digit4 == digit2 - digit3:
#     print('ДА')
# else: print ('НЕТ')

for i in range(1, 4):
    for j in range(3, 5):
        print(i + j, end='')
