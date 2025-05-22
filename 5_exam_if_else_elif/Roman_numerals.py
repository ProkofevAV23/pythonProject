# Программа, которая считывает целое число и выводит соответствующую ему римскую цифру.
# Если число находится вне диапазона 1−10, то программа должна вывести текст «ошибка».
# В таблице приведены римские цифры для чисел от 1 до 10.

x = int(input())

if x == 1:
    print('I')
elif x == 2:
    print('II')
elif x == 3:
    print('III')
elif x == 4:
    print('IV')
elif x == 5:
    print('V')
elif x == 6:
    print('VI')
elif x == 7:
    print('VII')
elif x == 8:
    print('VIII')
elif x == 9:
    print('IX')
elif x == 10:
    print('X')
else:
    print('ошибка')

