import sys
sys.stdin = open('1260.txt', 'r')
from collections import deque
# 정점, 간선, 시작 노드
n, m, s = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for g in graph:
    g.sort()
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visited = [False for _ in range(n+1)]

# bfs
def bfs(i):
    visited = [False for _ in range(n + 1)]
    que = deque([i])
    visited[i] = True
    while que:
        node = que.popleft()

        for nextNode in graph[node]:
            if not visited[nextNode]:
                que.append(nextNode)
                visited[nextNode] = True
# dfs
def dfs(i):
    if visited[i]:
        return
    visited[i] = True
    print(i, end=' ')
    for node in graph[i]:
        if not visited[node]:
            dfs(node)


dfs(s)
print()
bfs(s)


