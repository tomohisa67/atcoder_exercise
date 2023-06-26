import io
import sys
INPUT = """\
10
"""
sys.stdin = io.StringIO(INPUT)

N = int(input())

ans = N // 3 + N // 5 - N // 15

print(ans)