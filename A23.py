import io
import sys
_INPUT = """\
3 4
0 0 1
0 1 0
1 0 0
1 1 0
"""
sys.stdin = io.StringIO(_INPUT)

import numpy as np

N, M = map(int, input().split())
A = np.empty((0, N), dtype=int)
for i in range(M):
    a = np.array(list(map(int, input().split())))
    A = np.vstack((A, a))
# print(A)

tmp = np.sum(A, axis=0)
if np.count_nonzero(tmp) != N:
    print(-1)
    exit()

# S = [0] * N
# for i in range(1, M):
#     idx = np.where(A[i] == 1)
#     S[i-1] = 
idx, = np.where(A[0] == 1)
print(idx)

