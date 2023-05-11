import io
import sys
import bisect

_INPUT = """\
7 50
11 12 16 22 27 28 31
"""
sys.stdin = io.StringIO(_INPUT)

def binary_search(A, K):
    left = 0
    right = len(A) - 1
    while left < right:
        mid = (left + right) // 2
        if A[mid] < K:
            left = mid + 1
        elif A[mid] == K:
            return mid
        else:
            right = mid
    return left

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = [A[0]]
for i in range(1, N):
    B.append(B[i-1] + A[i])
# print(B)
ans = 0
for i in range(N):
    ind = binary_search(B, K)
    # ind = bisect.bisect_right(B,K)
    # print(ind)
    ans += ind - i
    K += A[i]
print(ans)
