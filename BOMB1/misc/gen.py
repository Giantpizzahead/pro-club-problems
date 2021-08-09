import random

random.seed(3724789236785637)

colors = ['red', 'red', 'red', 'red', 'white', 'white', 'white', 'white', 'blue', 'blue', 'blue', 'blue', 'orange', 'yellow', 'green', 'purple', 'black']

def gen_bomb(fin):
    wires = [random.choice(colors) for _ in range(3)]
    for w in wires:
        fin.write(w + '\n')

for i in range(6, 101):
    fin = open('subtasks/main/{:03}.in'.format(i), 'w')
    gen_bomb(fin)
    fin.close()
