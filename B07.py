import io
import sys

_INPUT = """\
10
7
0 3
2 4
1 3
0 3
5 6
5 6
5 6
"""
sys.stdin = io.StringIO(_INPUT)

T = int(input())
N = int(input())

inc = [0] * T
dec = [0] * T

for i in range(N):
    L, R = map(int, input().split())
    if L == T:
        continue
    elif R == T:
        inc[L] += 1
    else:
        inc[L] += 1
        dec[R] += 1

num = 0
for i in range(T):
    num = num + inc[i] - dec[i]
    print(num) 


