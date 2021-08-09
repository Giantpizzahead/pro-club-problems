import random

N = 3000
MAXA = 3000
Q = 200000

A = [random.randint(1, MAXA) for i in range(N)]
for i in range(N):
    if i < 500 or i > 2499:
        A[i] = i%2*2999+1
    else:
        A[i] = i+1
    # if random.randint(1, 2) == 1:
    #     A[i] = random.randint(990, 1010)
L = []
R = []
vis = set()
for i in range(Q):
    while True:
        a = random.randint(1, 500)
        b = random.randint(2501, 3000)
        #a = random.randint(1, N)
        #b = random.randint(1, N)
        if a > b:
            c = a
            a = b
            b = c
        if (a, b) in vis: continue
        L.append(a)
        R.append(b)
        vis.add((a, b))
        break

with open("/mnt/c/Users/sunny/Google Drive/Problem Making/problem_info/PRA7/subtasks/02_bonus/05.in", 'w') as fout:
    fout.write(str(N) + '\n')
    for i in range(N):
        if i != 0: fout.write(' ')
        fout.write(str(A[i]))
    fout.write('\n' + str(Q) + '\n')
    for i in range(Q):
        fout.write(str(L[i]) + ' ' + str(R[i]) + '\n')
