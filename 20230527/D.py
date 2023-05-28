import io
import sys
INPUT = """\
1 3 3
AAaA
"""
sys.stdin = io.StringIO(INPUT)

X, Y, Z = map(int, input().split())
S = input()

CapsLock = False

t = 0
for i in range(len(S)):
    if CapsLock:
        if S[i] == 'A':
            if X < Z + Y:
                t += X
            elif X > Z + Y:
                t += Z + Y
                CapsLock = False
        elif S[i] == 'a':
            if Y < Z + X:
                t += Y
            elif Y > Z + X:
                t += Z + X
                CapsLock = False
    else:
        if S[i] == 'A':
            if Y < Z + X:
                t += Y
            elif Y > Z + X:
                t += Z + X
                CapsLock = True
        elif S[i] == 'a':
            if X < Z + Y:
                t += X
            elif X > Z + Y:
                t += Z + Y
                CapsLock = True
print(t)