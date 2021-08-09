import random

N = int(input())
R = list(map(int, input().split()))
best = 0
for i in range(N):
    if R[i] > R[best]:
        best = i
S = []
for i in range(N):
    S.append(input().strip())

Q = int(input())
T = []
for i in range(Q):
    T.append(input().strip())

for query in T:
    print(best+1)
