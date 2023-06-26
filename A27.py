import io
import sys
_INPUT = """\
123 777
"""
sys.stdin = io.StringIO(_INPUT)

def swap(A, B):
    if A < B:
        tmp = A
        A = B
        B = tmp
    return A, B

def gcd(A, B):
    A, B = swap(A, B)
    for _ in range(10**9):
        rem = A % B
        if rem == 0:
            break
        A = B
        B = rem
    return B

A, B = map(int, input().split())
ans = gcd(A, B)
print(ans)