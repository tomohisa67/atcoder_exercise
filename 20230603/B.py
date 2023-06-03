import io
import sys
INPUT = """\
20230603
"""
sys.stdin = io.StringIO(INPUT)

N = int(input())

if N < 1e+3:
    print(N)
elif 1e+3 <= N < 1e+4:
    print(int(N//10 * 10))
elif 1e+4 <= N < 1e+5:
    print(int(N//100 * 100))
elif 1e+5 <= N < 1e+6:
    print(int(N//1e+3 * 1e+3))
elif 1e+6 <= N < 1e+7:
    print(int(N//1e+4 * 1e+4))
elif 1e+7 <= N < 1e+8:
    print(int(N//1e+5 * 1e+5))
elif 1e+8 <= N < 1e+9:
    print(int(N//1e+6 * 1e+6))
