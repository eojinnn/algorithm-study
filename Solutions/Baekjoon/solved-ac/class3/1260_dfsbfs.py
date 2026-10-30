import sys
from collections import deque
input = sys.stdin.readline
n, m, v = map(int, input().split())
visited = [0] * (n+1)

g = [[0]*(n+1) for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    g[a][b] = 1
    g[b][a] = 1

print(g)
def dfs(v):
    visited[v] = 1
    print(v, end = ' ')
    for nx in range(n+1):
        if visited[nx] == 0 and g[v][nx] == 1:
            dfs(nx)
dfs(v)

print()

visited = [0] * (n+1)
Q = deque([v])
visited[v] = 1
while Q:
    c = Q.popleft()
    print(c, end = ' ')
    for nx in range(1,n+1):
        if visited[nx] == 0 and g[c][nx] == 1:
            Q.append(nx)
            visited[nx] = 1


