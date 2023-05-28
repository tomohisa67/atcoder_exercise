import io
import sys
INPUT = """\
3
l0w
1ow
"""
sys.stdin = io.StringIO(INPUT)

N = int(input())
S = input()
T = input()

def same_moji(a, b):
    if a == b:
        return True
    elif a == '0' and b == "o":
        return True
    elif a == 'o' and b == "0":
        return True
    elif a == '1' and b == 'l':
        return True
    elif a == 'l' and b == '1':
        return True
    return False

for i in range(N):
    if same_moji(S[i], T[i]):
        continue
    print("No")
    exit()
print("Yes")