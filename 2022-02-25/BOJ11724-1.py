from collections import deque
import sys
sys.stdin = open('11724.txt', 'r')
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
result = 0


def bfs(x):
    que = deque([x])
    visited[x] = True
    while que:
        now = que.popleft()
        for _next in graph[now]:
            if not visited[_next]:
                que.append(_next)
                visited[_next] = True

    return 1


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    if not visited[i]:
        result += bfs(i)
print(result)