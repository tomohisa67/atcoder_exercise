import io
import sys

_INPUT = """\
5 4
1 2
2 3
3 4
3 5
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(M)]

G = [list() for i in range(N+1)]
for a, b in edges:
	G[a].append(b) 
	G[b].append(a) 

ind = [i for i in range(N+1)]
G = dict(zip(ind, G))

for i in range(1,N+1):
    output = ', '.join(map(str, G[i]))
    print(str(i) + ':' + '{' + output + '}')