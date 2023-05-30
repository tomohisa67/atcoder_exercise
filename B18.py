import io
import sys
_INPUT = """\
3 7
2 2 3
"""
sys.stdin = io.StringIO(_INPUT)

N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0] * (S+1) for _ in range(N+1)]
dp[0][0] = True
for j in range(1, S+1):
    dp[0][j] = False

for i in range(1, N+1):
    for j in range(S+1):
        if j < A[i-1]:
            dp[i][j] = dp[i-1][j]
        else:
            if dp[i-1][j-A[i-1]] == True or dp[i-1][j] == True:
                dp[i][j] = True
            else:
                dp[i][j] = False

Answer = []
H = N
W = S
while True:
    if H == 0:
        break
    if dp[H-1][W] == dp[H][W]:
        H = H - 1
    else:
        W = W - A[H-1]
        H = H - 1
        Answer.append(H)
Answer.reverse()

if dp[N][S] == True:
    Answer2 = [str(i+1) for i in Answer]
    print(len(Answer))
    print(" ".join(Answer2))
else:
    print(-1)