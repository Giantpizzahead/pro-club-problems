import random
rng = random.SystemRandom()

N = 3000
x_range = 100000000
y_range = 100000000

def gen_loc(i):
    return rng.randint(-x_range, x_range), rng.randint(-y_range, y_range)

used = set()
with open("PRI4/subtasks/02_bonus/05.in", 'w') as fout:
    fout.write(str(N) + '\n')
    for i in range(N):
        while True:
            x, y = gen_loc(i)
            if (x, y) in used: continue
            used.add((x, y))
            fout.write(str(x) + ' ' + str(y) + '\n')
            break
