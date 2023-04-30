import io
import sys

_INPUT = """\
7 10
11 12 16 22 27 28 31
"""
sys.stdin = io.StringIO(_INPUT)

def check(left, right, K):
    if K >= left-right:
        return True
    else:
        return False

N, K = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    left = i
    right = N-1
    init = A[i]
    d = []
    while left < right:
        mid = (left + right) // 2
        if K >= A[mid] - init:
            left = mid + 1
        else:
            right = mid
    d.append(left)
