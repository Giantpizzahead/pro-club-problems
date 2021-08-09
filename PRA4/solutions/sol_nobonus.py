"""
Try making every person impostor.
Runtime: O(NM)
"""

N = int(input())
names = {}
i_to_names = []
for i in range(N):
    s = input().strip()
    i_to_names.append(s)
    names[s] = i

A = []
B = []
I = []
M = int(input())
for i in range(M):
    s = input().strip().split()
    A.append(names[s[0]])
    B.append(names[s[2]])
    I.append(s[4] == 'impostor')

# Try each impostor
impostors = []
for i in range(N):
    possible = True
    for j in range(M):
        if A[j] == i:
            # Ignore info
            continue
        if I[j] and B[j] != i:
            # Info doesn't match
            possible = False
            break
        if not I[j] and B[j] == i:
            # Info doesn't match
            possible = False
            break
    if possible:
        impostors.append(i)

'''
print(names)
print(i_to_names)
print(A)
print(B)
print(I)
'''

print(len(impostors))
for i in impostors:
    print(i_to_names[i])
