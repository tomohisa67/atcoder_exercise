import io
import sys
_INPUT = """\
yyyyy
kyoto
"""
sys.stdin = io.StringIO(_INPUT)

S = input()
T = input()
M = [[0] * (len(T)) for _ in range(len(S))]

for i in range(len(S)):
    for j in range(len(T)):
        if i == 0 and j == 0:
            M[i][j] = 1 if S[i] == T[j] else 0
        elif i == 0:
            M[i][j] = M[i][j-1] + 1 if S[i] == T[j] else M[i][j-1]
        elif j == 0:
            M[i][j] = M[i-1][j] + 1 if S[i] == T[j] else M[i-1][j]
        elif S[i] == T[j]:
            M[i][j] = max(M[i-1][j] + 1, M[i][j-1])
        else:
            M[i][j] = max(M[i-1][j], M[i][j-1])

print(M[len(S)-1][len(T)-1])
