import io
import sys

_INPUT = """\
6 6
1 4
2 3
3 4
5 6
1 2
2 4
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(M)]

G = [list() for i in range(N+1)]
for a, b in edges:
	G[a].append(b) 
	G[b].append(a) 
	
print(G)

flag = 0
if flag != 0:
    print("The graph is connected.")
else:
    print("The graph is not connected.")