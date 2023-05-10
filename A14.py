import io
import sys

_INPUT = """\
3 50
3 9 17
4 7 9
10 20 30
1 2 3
"""
sys.stdin = io.StringIO(_INPUT)

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

