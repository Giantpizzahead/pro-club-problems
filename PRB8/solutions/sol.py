N = int(input())

arr = list(map(int, input().split()))

score_sum = 0
num_forgot = 0
for x in arr:
    if x == -1:
        num_forgot += 1
    else:
        score_sum += x

print(score_sum)
print(score_sum + 100 * num_forgot)
