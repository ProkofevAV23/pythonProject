# Программа, которая подсчитывает сумму введённых чисел (не включая само число n)

n = int(input())
sm = 0

for i in range(n):
    a = int(input())
    sm = sm + a
print(sm)
