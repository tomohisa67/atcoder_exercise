import io
import sys
INPUT = """\
5 5
ezzzz
zkzzz
ezuzs
zzznz
zzzzs
"""
sys.stdin = io.StringIO(INPUT)
# ----------------------------------------------------------

H, W = map(int, input().split())
S = [input() for _ in range(H)]

def check_string_exists(grid, target):
    h = len(grid)
    w = len(grid[0])

    # 縦方向のチェック
    for i in range(h):
        for j in range(w):
            # 下縦方向のチェック
            if i + len(target) <= h:
                exists = True
                for k in range(len(target)):
                    if grid[i+k][j] != target[k]:
                        exists = False
                        break
                if exists:
                    return "down", i, j
            # 上縦方向のチェック
            if i - len(target) >= -1:
                exists = True
                for k in range(len(target)):
                    if grid[i-k][j] != target[k]:
                        exists = False
                        break
                if exists:
                    return "up", i, j

    # 横方向のチェック
    for i in range(h):
        for j in range(w):
            # 右横方向のチェック
            if j + len(target) <= w:
                exists = True
                for k in range(len(target)):
                    if grid[i][j+k] != target[k]:
                        exists = False
                        break
                if exists:
                    return "right", i, j
            # 左横方向のチェック
            if j - len(target) >= -1:
                exists = True
                for k in range(len(target)):
                    if grid[i][j-k] != target[k]:
                        exists = False
                        break
                if exists:
                    return "left", i, j

    # 右斜め方向のチェック
    for i in range(h):
        for j in range(w):
            if i + len(target) <= h and j + len(target) <= w:
                exists = True
                for k in range(len(target)):
                    if grid[i+k][j+k] != target[k]:
                        exists = False
                        break
                if exists:
                    return "right_down", i, j
            if i - len(target) >= -1 and j + len(target) <= w:
                exists = True
                for k in range(len(target)):
                    if grid[i-k][j+k] != target[k]:
                        exists = False
                        break
                if exists:
                    return "right_up", i, j

    # 左斜め方向のチェック
    for i in range(h):
        for j in range(w):
            if i + len(target) <= h and j - len(target) >= -1:
                exists = True
                for k in range(len(target)):
                    if grid[i+k][j-k] != target[k]:
                        exists = False
                        break
                if exists:
                    return "left_down", i, j
            if i - len(target) >= -1 and j - len(target) >= -1:
                exists = True
                for k in range(len(target)):
                    if grid[i-k][j-k] != target[k]:
                        exists = False
                        break
                if exists:
                    return "left_up", i, j
    return False

direction, i, j = check_string_exists(S, "snuke")
if direction == "down":
    for _ in range(len("snuke")):
        print(i+1, j+1)
        i += 1
elif direction == "up":
    for _ in range(len("snuke")):
        print(i+1, j+1)
        i -= 1
elif direction == "right":
    for _ in range(len("snuke")):
        print(i+1, j+1)
        j += 1
elif direction == "left":
    for _ in range(len("snuke")):
        print(i+1, j+1)
        j -= 1
elif direction == "right_down":
    for _ in range(len("snuke")):
        print(i+1, j+1)
        i += 1
        j += 1
elif direction == "right_up":
    for _ in range(len("snuke")):
        print(i+1, j+1)
        i -= 1
        j += 1
elif direction == "left_down":
    for _ in range(len("snuke")):
        print(i+1, j+1)
        i += 1
        j -= 1
elif direction == "left_up":
    for _ in range(len("snuke")):
        print(i+1, j+1)
        i -= 1
        j -= 1
else:
    print("Not found")
