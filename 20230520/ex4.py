import io
import sys
INPUT = """\
2 3 2
3 10
2 5 15
"""
sys.stdin = io.StringIO(INPUT)
# ----------------------------------------------------------
N, M, D = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

def binary_search(A, v):
    left = 0
    right = len(A) - 1
    while left < right:
        mid = (left + right) // 2
        if A[mid] < v:
            left = mid + 1
        else:
            right = mid
    return left

maxv = 0
for j in reversed(range(M)):
    flag = 0
    idx = binary_search(A, B[j])
    for i in range(idx, len(A)):
        if abs(A[i] - B[j]) > D:
            i -= 1
            break
        value = A[i] + B[j]
        if maxv < value:
            maxv = value
    if maxv == 0:
        for i in reversed(range(idx)):
            if abs(A[i] - B[j]) > D:
                i += 1
                break
        value = A[i] + B[j]
        if maxv < value:
            maxv = value
    A = A[:i+1]
    if maxv > 0:
        break
print(maxv)