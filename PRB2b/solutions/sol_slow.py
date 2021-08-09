N = int(input())
points = list(map(int, input().split()))
K = int(input())

curr_sum = 0
if K < N / 2:
    curr_sum = sum(points)
    for i in range(K):
        x = min(points)
        curr_sum -= x
        points.remove(x)
else:
    for i in range(N-K):
        x = max(points)
        curr_sum += x
        points.remove(x)

print(curr_sum)
