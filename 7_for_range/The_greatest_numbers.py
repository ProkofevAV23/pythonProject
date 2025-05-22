# Программа, которая выводит два наибольших числа последовательности, каждое на отдельной строке

n = int(input())
largest = 2
second_largest = 2

for i in range(1, n+1):
    num = int(input())
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print(largest)
print(second_largest)
