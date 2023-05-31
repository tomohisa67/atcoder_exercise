import io
import sys

_INPUT = """\
3
10 20 30
35 40 33
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

ans = 0
for i in range(N):
    ans += A[i] * B[N-i-1]

print(ans)