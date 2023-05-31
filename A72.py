import io
import sys

_INPUT = """\
4 10 3
##...#.##.
.#....#...
##.####..#
#..######.
"""
sys.stdin = io.StringIO(_INPUT)

def find_max_index(lst):
    max_value = max(lst)
    max_index = lst.index(max_value)
    return max_index, max_value

H, W, K = map(int, input().split())
S = [list(input()) for _ in range(H)]
ans = 0

for k in range(K):
    row = []
    col = []
    for i in range(H):
        count = 0
        for j in range(W):
            if S[i][j] == '.':
                count += 1
        row.append(count)
    row_i, row_v = find_max_index(row)
    for j in range(W):
        S[row_i][j] = '#'

    for i in range(W):
        count = 0
        for j in range(H):
            if S[j][i] == '.':
                count += 1
        col.append(count)
    col_j, col_v = find_max_index(col)
    for i in range(H):
        S[i][col_j] = '#'
    
    if row_v >= col_v:
        max_i = row_i
        max_v = row_v
    else:
        max_j = col_j
        max_v = col_v

    ans += max_v

print(ans)

for v in itertools.product([ 0, 1 ], repeat = 4):
    print(v)