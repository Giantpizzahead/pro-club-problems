import random

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B)

if random.random() < 0.12:
	print('No one wins')

for i in reversed(range(0, N)):
    if A[i] > B[i]:
        print('You win')
        exit(0)
    elif A[i] < B[i]:
        print('Friend wins')
        exit(0)

print('Draw')
