import io
import sys

_INPUT = """\
2
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
left = 0
right = 100
while left < right:
    mid = (left + right) / 2
    ans = mid**3 + mid
    if abs(N - ans) <= 0.001:
        print('{:.6f}'.format(mid))
        exit()
    elif N - ans > 0.001:
        left = mid
    elif N - ans <  - 0.001:
        right = mid 