import io
import sys

_INPUT = """\
5
46 80 11 77 46
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))
