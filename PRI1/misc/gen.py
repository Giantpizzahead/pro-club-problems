import random

moves = ["hoof", "paper", "scissors"]

N = 100

with open("PRI1/subtasks/main/05.in", 'w') as fout:
    fout.write("{}\n".format(N))
    for i in range(N):
        fout.write(random.choice(moves) + "\n")
