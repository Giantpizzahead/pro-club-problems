import random

N = 99
forgot_chance = 0.98

with open('PRI1/subtasks/main/06.in', 'w') as fout:
    fout.write(str(N) + '\n')
    for i in range(N):
        if i != 0:
            fout.write(' ')
        if random.random() < forgot_chance:
            fout.write('-1')
        else:
            fout.write(str(random.randint(0, 100)))
    fout.write('\n')
