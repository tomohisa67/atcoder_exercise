import io
import sys
INPUT = """\
9 4
3 2
6 -1
1 6
6 5
-2 -3
5 3
2 -3
2 1
2 6
"""
sys.stdin = io.StringIO(INPUT)

from scipy.spatial import distance_matrix
import numpy as np

def get_infected(idx, dist_infected, Answer, N):
    for i in range(N):
        if dist_infected[idx, i] == 1 and Answer[i] == 0:
            Answer[i] = 1
            get_infected(i, dist_infected, Answer, N)
    return Answer

N, D = map(int, input().split())
points = []
Answer = [0] * N
Answer[0] = 1
for i in range(N):
    x, y = map(int, input().split())
    points.append([x, y])

points = np.array(points)
dist = distance_matrix(points, points)
dist_infected = np.where(dist <= D, 1, 0)
for i in range(N):
    for j in range(N):
        if i == j:
            dist_infected[i, j] = 0

Answer = get_infected(0, dist_infected, Answer, N)

print(dist_infected)

for i in range(N):
    if Answer[i] == 1:
        print("Yes")
    else:
        print("No")