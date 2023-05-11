import io
import sys

_INPUT = """\
15
83 31 11 17 32 19 23 37 43 47 53 61 67 5 55
5
10
20
30
40
50
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))
A.sort()
print(A)
Q = int(input())
for i in range(Q):
    x = int(input())
    left = 0
    right = N - 1
    while left < right:
        mid = (left + right) // 2
        if A[mid] >= x:
            right = mid
        else:
            left = mid + 1
    print(left)