import io
import sys
INPUT = """\
5 3
1 2 22
2 3 16
3 5 23
"""
sys.stdin = io.StringIO(INPUT)

D, N = map(int, input().split())

if N == 0:
    print(24 * D)
    exit()

day = [0] * D
for i in range(N):
    L, R, H = map(int, input().split())
    for k in range(L-1, R):
        if day[k] == 0:
            day[k] = H
        else:
            day[k] = min(day[k], H)

print(sum(day))