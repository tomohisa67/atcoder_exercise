import io
import sys
_INPUT = """\
6
30 10 60 10 60 50
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
h = list(map(int, input().split()))

dp = [0] * N
dp[1] = abs(h[1] - h[0])
for i in range(2, N):
    dp[i] = min(dp[i-1] + abs(h[i] - h[i-1]), dp[i-2] + abs(h[i] - h[i-2]))

Answer = []
Place = N-1
while True:
    Answer.append(Place)
    if Place == 0:
        break
    if dp[Place-1] + abs(h[Place] - h[Place-1]) == dp[Place]:
        Place = Place - 1
    else:
        Place = Place - 2
Answer.reverse()

# 答えを出力
Answer2 = [str(i+1) for i in Answer]
print(len(Answer))
print(" ".join(Answer2))