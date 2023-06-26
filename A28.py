import io
import sys
_INPUT = """\
4
+ 57
+ 43
* 100
- 1
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
ans = 0
for i in range(N):
    op, num = map(str, input().split())
    if op == "+":
        num = int(num)
        ans += num
    elif op == "-":
        num = int(num)
        ans -= num
    elif op == "*":
        num = int(num)
        ans *= num
    else:
        print("Error")
        break
    ans = ans % 10000
    print(ans)