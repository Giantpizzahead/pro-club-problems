import random

N = 200000
K = 101827

def gen_num(i):
    return random.randint(1, 1_000_000_000)

with open("PRB2-2/subtasks/02_bonus/05.in", 'w') as fout:
    fout.write(str(N) + '\n')
    for i in range(N):
        fout.write(str(gen_num(i)))
        random.random()
        fout.write(' ' if i != N-1 else '\n')
    fout.write(str(K) + '\n')
