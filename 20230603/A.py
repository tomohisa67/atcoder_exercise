import io
import sys
INPUT = """\
2
takahashi 1000000000
aoki 999999999
"""
sys.stdin = io.StringIO(INPUT)

N = int(input())
S = []
A = []
min_a = 1000000000
min_idx = 0
for i in range(N):
    s, a = map(str, input().split())
    S.append(s)
    A.append(int(a))
    if int(a) < min_a:
        min_a = int(a)
        min_idx = i

ans = S[min_idx:] + S[:min_idx]
for i in range(N):
    print(ans[i])

    