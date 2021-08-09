import random
import string
rng = random.SystemRandom()

N = 50000
Q = 50000
min_name_len = 18
max_r = 1000000000
query_distrib = [1]
for i in range(20):
    query_distrib.append((int)(1.0**i))
    #query_distrib.append((int)(1.3**(20-i)))
letter_distrib = []
for i in range(5):
    letter_distrib.append((int)(10**(i+1)))
for i in range(21):
    letter_distrib.append(1)

print("N =", N)
print("Q =", Q)
print("query_distrib =", query_distrib)
print("letter_distrib =", letter_distrib)

rng.shuffle(letter_distrib)
letters = []
for i in range(26):
    for j in range(letter_distrib[i]):
        letters.append(ord('a') + i)

def gen_letters(x):
    return ''.join(chr(rng.choice(letters)) for i in range(x))

R = []
for i in range(N):
    R.append(rng.randint(1, max_r))

W = []
names = set()
for i in range(N):
    while True:
        name = gen_letters(rng.randint(min_name_len, 20))
        if name not in names:
            names.add(name)
            W.append(name)
            break

chances = []
for i in range(len(query_distrib)):
    for j in range(query_distrib[i]):
        chances.append(i)

S = []
for i in range(Q):
    prefix_take = rng.randrange(0, N)
    while True:
        query_len = rng.choice(chances)
        if query_len > len(W[prefix_take]): continue
        query = W[prefix_take][:query_len]
        if query_len == 0:
            # Make a bad query
            query = gen_letters(rng.randint(1, 20))
        S.append(query)
        break

with open("PRA4b/subtasks/main/10.in", 'w') as fout:
    fout.write(str(N) + '\n')
    for i in range(N):
        if i != 0: fout.write(' ')
        fout.write(str(R[i]))
    fout.write('\n')
    for i in range(N):
        fout.write(W[i] + '\n')
    fout.write(str(Q) + '\n')
    for i in range(Q):
        fout.write(S[i] + '\n')
