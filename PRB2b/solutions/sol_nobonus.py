N = int(input())

P = list(map(int, input().split()))

if len(P) != N:
    exit(1)

min_points = min(P)
print(sum(P) - min_points)
