import io
import sys
INPUT = """\
77777 44444
"""
sys.stdin = io.StringIO(INPUT)

n, r = map(int, input().split())

C = 1000000007

num = min(n-r, r)
ans = 1
for i in range(num):
    ans = (ans * (n-i)) % C
    ans = (ans * pow(i+1, C-2, C)) % C

print(ans)