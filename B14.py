import io
import sys

_INPUT = """\
6 30
5 1 18 7 2 9
"""
sys.stdin = io.StringIO(_INPUT)

def binary_search(A, X):
    left = 0
    right = len(A) - 1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == X:
            return -1
        elif A[mid] > X:
            right = mid - 1
        else:
            left = mid + 1
    return left

N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
B = [A[0]]
for i in range(1, N):
    B.append(B[i-1] + A[i])

def find_conbination_K(B, K):
    if len(B) == 1: # 見つからなかった場合
        return -1
    p = binary_search(B, K)
    if p == -1:
        return 1
    K_prime = K - B[p]
    if find_conbination_K(B[:p], K_prime) == -1:
        if p+1 >= len(B):
            return -1
        B = B[:p] + B[p+1:]
        return find_conbination_K(B, K)
    else: # 見つかった場合
        return 1

if find_conbination_K(B, K) == -1:
    print("No")
else:  
    print("Yes")
