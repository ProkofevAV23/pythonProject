# Программа, которая упорядочивает три числа от большего к меньшему.

a = int(input())
b = int(input())
c = int(input())

f = max(a, b, c)
g = min(a, b, c)

print(f)
if b < a < c or c < a < b or a == b or a == c:
    print(a)
elif a < b < c or c < b < a or b == a or b == c:
    print(b)
elif a < c < b or b < c < a or c == a or c == b:
    print(c)
print(g)



