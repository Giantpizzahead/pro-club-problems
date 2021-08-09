import sys
import random

K = int(input())

answer_path = sys.argv[2]
with open(answer_path, 'r') as fans:
    ans_K = int(fans.readline())
    if K != ans_K:
        print(0)
        exit(0)
    # K is correct; is this a bonus test?
    ans_C = list(map(int, fans.readline().strip().split()))
    if ans_K == 0 or ans_C[0] == -1:
        print(1)
        exit(0)
    # Check if C is correct
    C = list(map(int, input().strip().split()))
    if len(C) != ans_K:
        print(0)
        exit(0)
    for i in range(ans_K):
        if C[i] != ans_C[i]:
            print(0)
            exit(0)
    # Correct!
    print(1)
