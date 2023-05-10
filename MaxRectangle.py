import io
import sys
from itertools import combinations
import numpy as np
_INPUT = """\
268920688 225068177
5
230851684 93756009 230851684 216640795
252914492 22788021 252914492 105724470
195274625 42252556 259418111 42252556
43425514 160876584 43425514 212921654
147608687 200254664 226610628 200254664
"""
sys.stdin = io.StringIO(_INPUT)

def find_maxh(y_list):
    maxh = 0
    y_old = 0
    count = 0
    for y in y_list:
        if count == 0:
            maxh = max(y[1] - y_old, maxh)

        if y[0] == 0:
            count += 1
        elif y[0] == 1:
            count -= 1

        y_old = y[1]
    return maxh

R, C = map(int, input().split())
N = int(input())

S = np.array([], dtype=int)
x = np.array([], dtype=int)
for i in range(N):
    a, b, c, d = map(int, input().split())
    if a == c: # 横線
        S = np.append(S, [0, a, b, d])
        x = np.append(x, a)
    elif b == d: # 縦線
        S = np.append(S, [1, b, a, c]) 
        x = np.append(x, [a, c])
S = S.reshape(N, 4)

x = np.append(x, [0, R])
x = np.unique(x)
lines = list(combinations(x, 2))
max_area = 0
for l in lines:
    y = np.array([], dtype=int)
    for s in S:
        # 指定した範囲に障害物が存在するなら，列情報をリストyに追加する
        if s[0] == 0 and s[1] > l[0] and s[1] < l[1]: # 横線
            y = np.append(y, [0, s[2]]) 
            y = np.append(y, [1, s[3]])
        elif s[0] == 1 and not (s[2] <= l[0] or s[3] >= l[1]): # 縦線
            y = np.append(y, [2, s[1]])
    y = np.append(y, [2, C])
    y = y.reshape(int(y.shape[0]/2), 2)
    J = np.argsort(y[:,1])
    y = y[J]
    maxh = find_maxh(y)
    area = maxh * (l[1] - l[0])
    max_area = max(area, max_area)
print(max_area)