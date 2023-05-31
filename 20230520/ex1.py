import io
import sys
INPUT = """\
7 3
"""
sys.stdin = io.StringIO(INPUT)
# ----------------------------------------------------------

A, B = map(int, input().split())
ans = A // B
if A % B == 0:
    ans = ans
else:
    ans = ans + 1
print(ans)