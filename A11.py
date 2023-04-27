import io
import sys

_INPUT = """\
15 47
11 13 17 19 23 29 31 37 41 43 47 53 59 61 67
"""
sys.stdin = io.StringIO(_INPUT)

N, X = map(int, input().split())
A = list(map(int, input().split()))

left = 0
right = N-1

while left <= right:
    mid = (left + right) // 2
    if A[mid] == X:
        print(mid+1)
        exit()
    elif A[mid] > X:
        right = mid - 1
    else:
        left = mid + 1
