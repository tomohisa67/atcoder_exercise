import io
import sys
INPUT = """\
4
0 0
0 1
1 0
1 1
"""
sys.stdin = io.StringIO(INPUT)

from scipy.spatial import distance

def dist_ij(i, j):
    return ((X[i] - X[j])**2 + (Y[i] - Y[j])**2)**0.5

N = int(input())
M = []
for _ in range(N):
    x, y = map(int, input().split())
    M.append([x, y])
D = distance.cdist(M, M, metric='euclidean')
print(D)
