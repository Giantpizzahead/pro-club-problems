import random

N = 5000
B = 2512
C = 2506

chance_0 = 2
chance_1 = 1
chance_2 = 1

choices = []
for i in range(chance_0): choices.append(0)
for i in range(chance_1): choices.append(1)
for i in range(chance_2): choices.append(2)

def gen_num(i):
    random.random()
    return random.choice(choices)

with open("PRA2/subtasks/02_bonus/08.in", 'w') as fout:
    fout.write("{} {} {}\n".format(N, B, C))
    for i in range(N):
        if i != 0:
            fout.write(' ')
        fout.write(str(gen_num(i)))
    fout.write("\n")
