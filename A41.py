import io
import sys
INPUT = """\
7
BBRRRBB
"""
sys.stdin = io.StringIO(INPUT)

N = int(input())
S = input()

def can_paint(S):
    for i in range(len(S)-2):
        if S[i] == S[i+1] == S[i+2]:
            return True
    return False

if can_paint(S):
    print('Yes')
else:
    print('No')