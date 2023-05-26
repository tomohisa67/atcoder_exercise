import io
import sys
_INPUT = """\
7
2 4 4 7 6 7
3 5 6 7 7 7
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        if j == A[i]:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + 100
        elif j == B[i]:
            dp[i][j] = dp[i-1][j-1] + 150
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])