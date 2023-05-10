import io
import sys
import numpy as np
_INPUT = """\
5
46 80 11 77 46
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))
A = np.array(A)
B = np.array([], dtype=int)

# print(A)
I = np.argsort(A)
# print(I)
A = A[I]
# print(A)
A_old = -1
num = 0
for i in range(N):
    if A_old != A[i]:
        num += 1
    B = np.append(B, num)
    A_old = A[i]
# print(B)
# B = B[I]
# for i in range(N):
#     B
b0 = B[0].copy()
b1 = B[1].copy()
b2 = B[2].copy()
b3 = B[3].copy()
b4 = B[4].copy()
B[0] = b1
B[1] = b4
B[2] = b0
B[3] = b3
B[4] = b2
print(B)
