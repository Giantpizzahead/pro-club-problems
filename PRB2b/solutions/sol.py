N = int(input())
points = list(map(int, input().split()))
K = int(input())

if len(points) != N:
    exit(1)

points.sort()

curr_sum = sum(points)

for i in range(K):
    curr_sum -= points[i]

print(curr_sum)
