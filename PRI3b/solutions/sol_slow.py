import math

N = int(input())

def is_prime(x):
    for i in range(2, x):
        if x % i == 0: return False
    return True

for d in range(N):
    if is_prime(N-d):
        print(N-d)
        break
    if is_prime(N+d):
        print(N+d)
        break
