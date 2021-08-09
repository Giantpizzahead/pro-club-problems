import random

N = 50
S = random.randint(1, 3)

with open("PRB2/subtasks/main/04.in", 'w') as fout:
    fout.write("{} {}\n".format(N, S))
    for i in range(N):
        while True:
            a = random.randint(1, 3)
            b = random.randint(1, 3)
            if a != b:
                fout.write("{} {}\n".format(a, b))
                break