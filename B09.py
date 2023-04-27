import io
import sys

_INPUT = """\
2
1 1 3 3
2 2 4 4
"""
sys.stdin = io.StringIO(_INPUT)

import numpy as np
N = int(input())
Z = np.zeros((1501, 1501))

inc = np.zeros((1500,1500))
dec = np.zeros((1500,1500))
for i in range(N):
    a, b, c, d = map(int, input().split())
    inc[a-1][b-1] += 1
    dec[c-1][d-1] -= 1
    dec[a-1][d-1] -= 1
    dec[c-1][b-1] -= 1