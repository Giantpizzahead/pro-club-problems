N, S = map(int, input().split())

# Process all swaps
pea_loc = S
for i in range(N):
    a, b = map(int, input().split())
    if pea_loc == a:
        pea_loc = b
    elif pea_loc == b:
        pea_loc = a

print(pea_loc)
