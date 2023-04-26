import numpy as np
import io
import sys

_INPUT = """\
5 5 2
1 1 3 3
2 2 4 4
"""
sys.stdin = io.StringIO(_INPUT)


H, W, N = list(map(int, input().split()))

L = np.zeros((H,W), dtype=int)
R = np.zeros((H,W), dtype=int)
for i in range(N): 
    a, b, c, d = map(int, input().split())
    a = a - 1
    b = b - 1
    c = c - 1
    d = d - 1
    L[a][b] += 1
    R[c][d] += 1

Z = np.zeros((H,W), dtype=int)

