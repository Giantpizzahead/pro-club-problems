import random

N = 100

letters = "abcdefghijklmnopqrstuvwxyz"
names = set()

with open("PRB4a/subtasks/main/08.in", 'w') as fout:
    fout.write(str(N) + '\n')
    for i in range(N):
        while True:
            name = ''.join([random.choice(letters) for _ in range(random.randint(1, 10))])
            if name in names: continue
            score = random.randint(1337, 1357)
            fout.write("{} {}\n".format(name, score))
            break
