import random

N = 300

chars = '()[]{}'
chances = [1, 1, 1, 1, 1, 1]

choices = []
for i in range(6):
    for j in range(chances[i]):
        choices.append(chars[i])

def gen_paren(i):
    '''
    if random.random() < i / N:
        return '('
    else:
        return ')'
    '''
    if random.random() < i / N:
        return random.choice('([{')
    else:
        return random.choice(')]}')
    # return random.choice(choices)

with open("PRA3/subtasks/02_bonus/20.in", 'w') as fout:
    for i in range(N):
        fout.write(gen_paren(i))
    fout.write("\n")
