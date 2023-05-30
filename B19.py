import io
import sys
_INPUT = """\
4 7
3 13
3 17
5 29
1 10
"""
sys.stdin = io.StringIO(_INPUT)

import numpy as np
N, W = map(int, input().split())
w = []
v = []
for i in range(N):
    a, b = map(int, input().split())
    w.append(a)
    v.append(b)

dp = [[0]*(W+1) for _ in range(N+1)]
dp[1][w[0]] = v[0]
idx = [w[0]]
for i in range(2, N+1):
    for j in idx:
        dp[i][j] = max(dp[i-1][j], dp[i][j])
        if j + w[i-1] <= W:
            dp[i][j + w[i-1]] = max(dp[i-1][j + w[i-1]], dp[i-1][j] + v[i-1])
            idx.append(j + w[i-1])
        else:
            dp[i][w[i-1]] = max(dp[i-1][w[i-1]], dp[i-1][j] + v[i-1])


# print(max(dp[N]))
# print(dp[N][W])

print(np.array(dp))