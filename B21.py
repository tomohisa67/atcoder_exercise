import io
import sys
_INPUT = """\
11
programming
"""
sys.stdin = io.StringIO(_INPUT)
# 11
# programming

def find_palindrome(S):
    length = 0
    # i = 0
    # while len(S) > 0 and i <= 4:
    #     if not S[i] in S[i+1:]:
    #         S = S[:i] + S[i+1:]
    #         continue
    #     i += 1
    #     print(S)
    for i in range(len(S)-1):
        if not S[i] in S[i+1:]:
            S[i] = '.'
        # else:
            
    return length

N = int(input())
S = list(input())

idx = []
for i in range(len(S)-1):
    if not S[i] in S[i+1:] and not S[i] in S[:i]:
        S[i] = '.'
        idx.append(i)

S_new = [S[i] for i in range(len(S)) if i not in idx]

print(S_new)

# print(find_palindrome(S))