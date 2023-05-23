import io
import sys

_INPUT = """\
5
2 4 1 3
5 3 7
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

T = [0] * N
for i in range(1, N):
    if i == 1:
        T[i] = A[i-1]
    else:
        T[i] = min(T[i-1] + A[i-1], T[i-2] + B[i-2])

print(T[N-1])
