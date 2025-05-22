# Вводятся 3 строки в случайном порядке.
# Программа, которая выясняет, можно ли из длин этих строк построить арифметическую прогрессию.

a = input()
c = input()
e = input()

b = len(a)
d = len(c)
f = len(e)

h = min(b, d, f)
g = max(b, d, f)
mid = b+d+f-h-g

if g - mid == mid - h:
    print('YES')
else:
    print('NO')

