import io
import sys
INPUT = """\
4
20 10 30 40
"""
sys.stdin = io.StringIO(INPUT)


N = int(input())
A = list(map(int, input().split()))

Answer = []
for i in range(N):
    tmp = []
    for j in range(N-i-1):
        tmp.append(max(A[j], A[j+1]))
    A = tmp.copy()

print(A)