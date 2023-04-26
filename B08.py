import numpy as np
import io
import sys

_INPUT = """\
5
1 3
2 5
3 4
2 6
3 3
3
1 3 3 6
1 5 2 6
1 3 3 5
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
P = np.zeros((1500,1500))
for i in range(N):
    x, y = map(int, input().split())
    P[x-1][y-1] += 1

Z = np.zeros((1500,1500))

for i in range(1500):
    for j in range(1500):
        if i == 0 and j == 0:
            Z[i][j] =  P[i][j]
        elif i == 0:
            Z[i][j] = Z[i][j-1] + P[i][j]
        elif j == 0:
            Z[i][j] = Z[i-1][j] + P[i][j]
        else:
            Z[i][j] = Z[i][j-1] + Z[i-1][j] - Z[i-1][j-1] + P[i][j]

Q = int(input())
for i in range(Q): 
    a, b, c, d = map(int, input().split())
    a = a - 1
    b = b - 1
    c = c - 1
    d = d - 1

    if a == 0 and b == 0:
        num = Z[c][d]
    elif a == 0:
        num = Z[c][d] - Z[c][b-1]
    elif b == 0:
        num = Z[c][d] - Z[a-1][d]
    else:
        num = Z[c][d] - Z[c][b-1] - Z[a-1][d] + Z[a-1][b-1] 
    print(int(num))

# _INPUT = """\
# 5
# 1 3
# 2 5
# 3 4
# 2 6
# 3 3
# 3
# 1 3 3 6
# 1 5 2 6
# 1 3 3 5
# """
