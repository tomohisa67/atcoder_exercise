import io
import sys

_INPUT = """\
4 10
1 2 3 4
"""
sys.stdin = io.StringIO(_INPUT)

N, K = map(int, input().split())
A = list(map(int, input().split()))

left = 1
right = K

while left <= right:
    t = (left + right) // 2
    x = 0
    for i in range(N):
        x += t // A[i]
    if x == K:
        print(t)
        exit()
    elif x > K:
        if right - left <= 1:
            print(t)
            exit()
        right = t - 1
    else:
        left = t + 1