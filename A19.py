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

N, W = map(int, input().split())
w, v = [], []
for _ in range(N):
    wi, vi = map(int, input().split())
    w.append(wi)
    v.append(vi)

import numpy as np
# dp = [[0] * (W+1) for _ in range(N+1)]
dp = np.zeros((N+1, W+1))
for i in range(1, N+1):
    for j in range(W+1):
        if dp[i-1][j] != 0:
            dp[i][j] = dp[i-1][j]
        if j - w[i-1] >= 0 and dp[i][j - w[i-1]] != 0:
            dp[i][j] = max(dp[i-1][j], dp[i][j - w[i-1]] + v[i-1])
maxv = max(dp[N])
print(dp)
print(maxv)
