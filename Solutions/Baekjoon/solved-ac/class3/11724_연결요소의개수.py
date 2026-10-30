"""
아이디어
visited 쭉 돌고 cnt +1 아직 그래프에 남은게 있다면 다시 visitied돌기
시간 복잡도

"""

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
# g = [[]]*(N+1) #곱하기는 같은 객체를 복사한것 다른 객체를 만드려면 반복문을 돌려야함.
g = [[] for i in range(N+1)]
visited = [0]*(N+1)
cnt = 0

for i in range(M):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

def dfs(n):
    visited[n] = 1
    for i in g[n]:      
        if visited[i] == 0:
            dfs(i)

for i in range(1, len(visited)):
    if visited[i] == 0:
        dfs(i)
        cnt += 1
print(cnt)


