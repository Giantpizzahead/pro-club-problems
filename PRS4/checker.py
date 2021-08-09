import sys
import random

N = int(input())
if N < 1 or N > 1000000:
    print(0)
    exit(0)

ans = 421337
answer_path = sys.argv[2]
with open(answer_path, 'r') as fans:
    M = int(fans.readline())
    dist = 0
    if N == ans:
        print(1)
        exit(0)
    elif M == 1:
        if N > ans:
            print(0)
            exit(0)
        else:
            dist = ans - N
    else:
        if N < ans:
            print(0)
            exit(0)
        else:
            dist = N - ans
    
    if dist > 4950:
        print(0.01)
    else:
        score = 0
        while dist > 0:
            score += 1
            dist -= score
        print((100 - score) / 100)
