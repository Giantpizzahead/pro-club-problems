import random

V = 9999

N = int(input())
print(N)
for i in range(N):
    a, b = map(int, input().split())
    a = a * 100000 + random.randint(-V, V)
    b = b * 100000 + random.randint(-V, V)
    a = max(0, a)
    a = min(10 ** 9, a)
    b = max(0, b)
    b = min(10 ** 9, b)
    print(str(a) + ' ' + str(b))
