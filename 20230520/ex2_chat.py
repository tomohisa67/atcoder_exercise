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


exists = check_string_exists(grid, target)