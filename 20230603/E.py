import io
import sys
INPUT = """\
6 6
1 2
2 3
2 3
3 1
5 4
5 5
3
1 5
2 6
4 3
4
2 5
2 6
5 6
5 4
"""
sys.stdin = io.StringIO(INPUT)

from collections import defaultdict

def is_connected(graph):
    start_node = list(graph.keys())[0]
    color = {v: 'white' for v in graph.keys()}
    color[start_node] = 'gray'

    def dfs(node):
        for neighbor in graph[node]:
            if color[neighbor] == 'white':
                color[neighbor] = 'gray'
                dfs(neighbor)
        color[node] = 'black'

    dfs(start_node)

    return list(color.values()).count('black') == len(graph)

N, M = map(int, input().split())
graph = defaultdict(list)
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
graph = dict(graph)
# print(graph)

K = int(input())
for i in range(K):
    x, y = map(int, input().split())
Q = int(input())
for i in range(Q):
    p, q = map(int, input().split())

