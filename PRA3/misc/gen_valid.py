import random

N = 1000000

chars = ['()', '[]', '{}']
chances = [1, 1, 1]
split_chance = 0.95

choices = []
for i in range(3):
    for j in range(chances[i]):
        choices.append(chars[i])

S = ['X' for _ in range(N)]

def fill_paren(i, j):
    parens = random.choice(choices)
    S[i] = parens[0]
    S[j] = parens[1]

def gen_valid(i, j):
    if j - i == 1:
        fill_paren(i, j)
        return
    if random.random() < split_chance:
        k = random.randint(i+1, j-2)
        if (k - i) % 2 == 0:
            k += 1
        gen_valid(i, k)
        gen_valid(k+1, j)
    else:
        fill_paren(i, j)
        gen_valid(i+1, j-1)

with open("PRA3/subtasks/01_main/10.in", 'w') as fout:
    gen_valid(0, N-1)
    for i in range(N):
        fout.write(S[i])
    fout.write("\n")
