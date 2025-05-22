# Даны названия трёх городов. Напишите программу, которая определяет самое короткое и самое длинное название города.

a = input()
c = input()
e = input()

b = len(a)
d = len(c)
f = len(e)

h = min(b, d, f)
g = max(b, d, f)

if h == b:
    print(a)
elif h == d:
    print(c)
else:
    print(e)
if g == b:
    print(a)
elif g == d:
    print(c)
else:
    print(e)

