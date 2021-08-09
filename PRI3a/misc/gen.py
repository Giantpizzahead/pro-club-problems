import random

N = 5000
A = 3918

used = [False for _ in range(N)]
used[0] = True

links = [0 for _ in range(N)]

curr_site = 0
for i in range(A-1):
    while True:
        next_site = random.randint(0, N-2)
        if not used[next_site]:
            break
    links[curr_site] = next_site + 1
    used[next_site] = True
    curr_site = next_site

links[curr_site] = N

for i in range(N):
    if not used[i]:
        links[i] = random.randint(1, N)

with open("PRB3/subtasks/main/10.in", 'w') as fout:
    fout.write("{}\n".format(N))
    fout.write(" ".join(str(x) for x in links) + '\n')
