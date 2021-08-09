import random
import string

N = 100000
P = 1
M = 75000
is_imp_chance = 0.99

names = set()
for i in range(N):
    while True:
        name = ''.join(random.choice(string.ascii_letters) for i in range(4))
        if name not in names:
            names.add(name)
            break

names = list(names)
names = sorted(names)
impostor = [False for _ in range(N)]
while P > 0:
    # loc = random.randrange(N)
    loc = 1000
    if not impostor[loc]:
        impostor[loc] = True
        P -= 1

with open("PRA4/subtasks/02_bonus/05.in", 'w') as fout:
    fout.write(str(N) + '\n')
    for i in range(N):
        fout.write(names[i] + '\n')
    fout.write(str(M) + '\n')
    for i in range(M):
        while True:
            A = random.randrange(N)
            random.random()
            B = random.randrange(N)
            is_imp = random.random()
            random.random()
            if A == B: continue

            if is_imp < is_imp_chance:
                if not impostor[A]:
                    B = 1000
                    if random.random() < 0.5:
                        temp = A
                        A = B
                        B = temp
                fout.write("{} says {} is impostor\n".format(names[A], names[B]))
                break
            else:
                if impostor[B]: continue
                fout.write("{} says {} is safe\n".format(names[A], names[B]))
                break

# print(names)
# print(impostor)
