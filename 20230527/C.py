import io
import sys
INPUT = """\
5 2 1 5
LDRLD
0 0
-1 -1
"""
sys.stdin = io.StringIO(INPUT)

N, M, H, K = map(int, input().split())
S = input()
x = 0
y = 0
Mx = []
My = []

for i in range(M):
    tmp_x, tmp_y = map(int, input().split())
    Mx.append(tmp_x)
    My.append(tmp_y)

for i in range(N):
    H -= 1
    # 生存判定
    if H < 0:
        print("No")
        exit()
    # 移動
    if S[i] == 'R':
        x += 1
    elif S[i] == 'L':
        x -= 1
    elif S[i] == 'U':
        y += 1
    elif S[i] == 'D':
        y -= 1
    # 移動先にアイテムがあるか判定
    if H < K and (x, y) in zip(Mx, My):
        H = K
        
print("Yes")

