# Программа, которая принимает целое число x и определяет, принадлежит ли данное число указанным промежуткам.

x = int(input())

if -2 >= x and x > -30 or (x > 7 and x <= 25):
    print('Принадлежит')
else: print ('Не принадлежит')


