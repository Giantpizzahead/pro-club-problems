import random

chars = '()[]{}'
chances = [1, 1, 1, 1, 1, 1]

choices = []
for i in range(6):
    for j in range(chances[i]):
        choices.append(chars[i])

def gen_paren(i):
    return random.choice(choices)

for j in range(10):
    with open("PRA3/subtasks/03_stress/{:03}.in".format(j), 'w') as fout:
        N = random.randint(1, 25)
        for i in range(N):
            fout.write(gen_paren(i))
        fout.write("\n")
