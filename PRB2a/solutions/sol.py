A, B, C = map(int, input().split())

print(A + B + C - min(min(A, B), C))
