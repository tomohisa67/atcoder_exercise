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

X = np.array([])
for i in range(N):
    coordinate = list(map(int, input().split()))
    if i == 0:
        X = coordinate
    else:
        X = np.vstack((X, coordinate))
    
A = X[:, 0]
B = X[:, 1]
C = X[:, 2]
D = X[:, 3]

print(min(A))