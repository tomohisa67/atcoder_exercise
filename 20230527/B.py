import io
import sys
INPUT = """\
10 10
4 10 7 2 8 3 9 1 6 5
3 6 2 9 1 8 10 7 4 5
9 3 4 5 7 10 1 8 2 6
7 3 1 8 4 9 5 6 2 10
5 2 1 4 10 7 9 8 3 6
5 8 1 6 9 3 2 4 7 10
8 10 3 4 5 7 2 9 6 1
3 10 2 7 8 5 1 4 9 6
10 6 1 5 4 2 3 8 9 7
4 5 9 1 8 2 7 6 3 10
"""
sys.stdin = io.StringIO(INPUT)

import numpy as np
N, M = map(int, input().split())
A = [[0] * N for _ in range(N)]
A = np.array(A)
for i in range(N):
    A[i][i] = 1

for i in range(M):
    a = list(map(int, input().split()))
    for j in range(1, N):
        A[a[j-1]-1][a[j]-1] = 1
        A[a[j]-1][a[j-1]-1] = 1

ans = np.count_nonzero(A == 0) // 2
print(ans)