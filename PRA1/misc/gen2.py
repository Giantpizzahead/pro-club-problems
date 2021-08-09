import random

N = 2000

A = []
B = []

for i in range(490):
    A.append(7930)
    B.append(7930)

for i in range(280):
    A.append(5187)
    B.append(5187)

for i in range(755):
    A.append(3002)
    B.append(3002)

for i in range(380):
    A.append(185)
    B.append(185)

for i in range(62):
    A.append(7)
    B.append(7)

B.append(7)

for i in range(32):
    A.append(2)
    B.append(2)

A.append(2)

random.shuffle(A)
random.shuffle(B)

with open('PRA1/subtasks/02_bonus/04.in', 'w') as fout:
    fout.write('{}\n'.format(N))
    fout.write(' '.join(str(x) for x in A) + '\n')
    fout.write(' '.join(str(x) for x in B) + '\n')
