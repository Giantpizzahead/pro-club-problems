import random

N = int(input())
R = list(map(int, input().split()))
S = []
for i in range(N):
    S.append(input().strip())

Q = int(input())
T = []
for i in range(Q):
    T.append(input().strip())

for query in T:
    ans = 0
    best = -1
    for i in range(N):
        if R[i] > best and S[i].startswith(query):
            ans = i
            best = R[i]
    print(ans+1)