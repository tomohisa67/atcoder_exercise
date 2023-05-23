import io
import sys
_INPUT = """\
4
4 20
3 30
2 40
1 10
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
P, A = [0], [0]
for _ in range(N):
    p, a = map(int, input().split())
    P.append(p)
    A.append(a)

dp = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        if i < P[i]:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + A[i])
        elif i > P[i] and j <= N-1:
            dp[i][j] = dp[P[i]][j+1]
        # if j < P[i]:
            # dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + A[i])
        # else:
        #     dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(dp[i][1:])
