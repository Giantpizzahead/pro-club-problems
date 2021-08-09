import sys
import random

N = int(input())
if N < 1 or N > 420000000:
    print(0)
    exit(0)

answer_path = sys.argv[2]
with open(answer_path, 'r') as fans:
    M = int(fans.readline())
    if N % M == 0:
        print(1)
    else:
        print(0)
