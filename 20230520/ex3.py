import io
import sys
INPUT = """\
8 4
fast
face
cast
race
fact
rice
nice
case
"""
sys.stdin = io.StringIO(INPUT)
# ----------------------------------------------------------
N, M = map(int, input().split())
S = [input() for _ in range(N)]

def edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)

    # 2次元のDPテーブルを作成
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # DPテーブルの初期化
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # DPテーブルを更新
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1

    # 編集距離を返す
    return dp[m][n]

def is_connected(vector):
    n = vector.shape[0]

    # 隣接行列を作成
    adjacency_matrix = vector

    # 連結判定
    connected = True
    for i in range(n):
        if not np.any(adjacency_matrix[i]):
            connected = False
            break

    return connected

import numpy as np
I = np.zeros((N, N), dtype=int)
for i in range(N):
    for j in range(N):
        if i != j:
            tmp = edit_distance(S[i], S[j])
            if tmp != 1:
                I[i][j] = 0
            else:
                I[i][j] = tmp
        else:
            I[i][j] = 0

if is_connected(I):
    print("Yes")
else:
    print("No")