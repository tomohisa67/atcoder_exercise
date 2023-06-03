import io
import sys
INPUT = """\
7 6
5
6 1
3 1
4 2
1 5
6 2
2
2 5
2
3 4
"""
sys.stdin = io.StringIO(INPUT)

import numpy as np

def binary_search(A, x):
    left = 0
    right = len(A)
    while left < right:
        mid = (left + right) // 2
        if x < A[mid]:
            right = mid
        else:
            left = mid + 1
    return left

W, H = map(int, input().split())
N = int(input())
Berry = np.array([])
for i in range(N):
    p, q = map(int, input().split())
    Berry = np.append(Berry, [p, q])
Berry = Berry.reshape(N, 2)
A = int(input())
a = list(map(int, input().split()))
B = int(input())
b = list(map(int, input().split()))

max_berry = 0
min_berry = N

# print(Berry)
sorted_indices = Berry[:, 0].argsort()
Berry = Berry[sorted_indices]
# print(Berry)
idx_old = 0
for i in range(A+1):
    # 縦線で区切る
    if i >= A:
        idx = N
    else:
        idx = binary_search(Berry[:, 0], a[i])
    tmpBerry = Berry[idx_old:idx, :]
    idx_old = idx
    # print()
    # print(tmpBerry)

    # 横線で区切る
    sorted_indices = tmpBerry[:, 1].argsort()
    tmpBerry = tmpBerry[sorted_indices]
    # print(tmpBerry)
    idx_old = 0
    for j in range(B+1):
        if j >= B:
            idx = len(tmpBerry)
        else:
            idx = binary_search(tmpBerry[:, 1], b[j])
        # print(idx)
        # print(tmpBerry[idx_old:idx, :])
        max_berry = max(max_berry, len(tmpBerry[idx_old:idx, :]))
        min_berry = min(min_berry, len(tmpBerry[idx_old:idx, :]))
        idx_old = idx

print(min_berry, max_berry)

