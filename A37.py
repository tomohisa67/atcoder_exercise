import io
import sys
INPUT = """\
2 3 100
10 20
1 2 3
"""
sys.stdin = io.StringIO(INPUT)

N, M, B = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

print(M*N*B + M*sum(A) + N*sum(C))