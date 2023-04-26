import io
import sys

_INPUT = """\
7
0 1 1 0 1 0 0
3
2 5
2 7
5 7
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))

atari = [0] * N

for i in range(N):
    if i == 0:
        atari[i] = A[0]
    else:
        atari[i] = atari[i-1] + A[i]

Q = int(input())
for i in range(Q):
    num = 0
    L, R = map(int, input().split())
    length = R - L + 1
    num = atari[R-1] - atari[L-1] + A[L-1] 
    if num > length - num:
        print("win")
    elif num < length - num:
        print("lose")
    else:
        print("draw")
