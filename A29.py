import io
import sys
_INPUT = """\
5 23
"""
sys.stdin = io.StringIO(_INPUT)

def power(a, b):
    return a ** b

a, b = map(int, input().split())
C = 1e+9 + 7

for j in range(1, b+1):
    if a >= C:
        break
    a *= a
r = a % C
t = b // j
r = r * t * power(a, b - j * t)

ans = int(r % C)

print(ans)