import random

N = 2000

used = [False for _ in range(2 * N + 1)]

def gen_num(i):
    # return (N-i)*2
    num = random.randint(1, 2 * N)
    while used[num]:
        num = random.randint(1, 2 * N)
    used[num] = True
    return num

with open('PRA1/subtasks/01_main/10.in', 'w') as fout:
    fout.write('{}\n'.format(N))
    for i in range(N):
        if i != 0:
            fout.write(' ')
        fout.write(str(gen_num(i)))
    fout.write('\n')
    for i in range(N):
        if i != 0:
            fout.write(' ')
        fout.write(str(gen_num(i)))
    fout.write('\n')
