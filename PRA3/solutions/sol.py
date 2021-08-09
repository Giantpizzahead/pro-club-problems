'''
 * dp[i][j] = Min deletions to fix program in [i, j]
 * 
 * Base:
 * dp[i][i] = 1
 * d[i][i+1] = 0 if match, else 2
 * 
 * Trans:
 * dp[i][j] =
 * if match -> dp[i+1][j-1]
 * for k in i...j-1 -> dp[i][k] + dp[k+1][j]
 * 
 * Answer:
 * dp[0][N-1]
 * 
 * Runtime: O(N^2)
'''
import time


S = input().strip()
N = len(S)
start = time.time()
print("N =", N)
def parenMatches(i, j):
    return S[i] == '(' and S[j] == ')' or S[i] == '[' and S[j] == ']' or S[i] == '{' and S[j] == '}'

dp = [[987654321 for _ in range(N)] for _ in range(N)]

for i in range(N):
    dp[i][i] = 1
for i in range(N-1):
    dp[i][i+1] = 0 if parenMatches(i, i+1) else 2

ops = 0
for r in range(2, N):
    for i in range(N-r):
        j = i + r
        if parenMatches(i, j):
            dp[i][j] = dp[i+1][j-1]
        for k in range(i, j):
            ops += 1
            dp[i][j] = min(dp[i][k] + dp[k+1][j], dp[i][j])

end = time.time()

print("# ops =", ops)
print("time = {:.3f} seconds".format(end-start))
if dp[0][N-1] == 0: print("YES")
else:
    print("NO")
    print(dp[0][N-1])
