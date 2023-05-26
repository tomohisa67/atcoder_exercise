import io
import sys
_INPUT = """\
6
2 3 1 6 4 5
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))
A = [0] + A

dp = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(i, N+1):
        if A[j-1] < A[j]:
            dp[i][j] = max(dp[i-1][j-1] + 1, dp[i][j-1])
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

# import numpy as np
# print(np.array(dp))
print(dp[N][N])


# S = [0] * (N+1)
# S[0] = A[0]
# for i in range(1, N+1):
#     if A[i-1] < A[i]:
#         S[i] = S[i-1] + 1
#     else:
#         S[i] = S[i-1]
#     print(S)

# # print(S)
# print(S[N])