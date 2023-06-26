import io
import sys
INPUT = """\
3
123 86399
1 86400
86399 86400
"""
sys.stdin = io.StringIO(INPUT)

import numpy as np

def is_bigger(l, r):
    if r <= l:
        return True
    else:
        return False

N = int(input())
S = np.array([list(map(int, input().split())) for _ in range(N)])
I = np.argsort(S[:, 0])
S = S[I]
# print(S)
count = 0

for i in range(1, N):
    if S[i-1][1] <= S[i][0]:
        count += 1
    else:
        
