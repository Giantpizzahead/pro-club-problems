import sys

fin = open(sys.argv[1], 'r')
fans = open(sys.argv[2], 'r')

N = int(fin.readline())
R = list(map(int, fin.readline().strip().split()))
W = []
for i in range(N):
    W.append(fin.readline().strip())
Q = int(fin.readline())
S = []
for i in range(Q):
    S.append(fin.readline().strip())
O = int(fans.readline())

# print(R)
# print(W)
# print(S)
# print(O)

P = 0
for i in range(Q):
    A = int(input()) - 1
    if W[A].startswith(S[i]):
        # This website works
        P += R[A]

if P == O:
    print(1)
else:
    print(float(P/O))
