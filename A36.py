import io
import sys
INPUT = """\
5 10
"""
sys.stdin = io.StringIO(INPUT)

N, K = map(int, input().split())

a = K - 2*(N-1)
if  a >= 0 and a%2 == 0:
    print('Yes')
else:
    print('No')