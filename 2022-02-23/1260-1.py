from collections import deque
import sys
sys.stdin = open('1260.txt', 'r')
n, m, s = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
stack, visited = [], [False] * n
result1, result2 = [], []
def dfs(i):
    visited[i] = True
    result1.append(i)
    for j in range(n):
        if graph[i][j] != 0 and not visited[j]:
            dfs(j)

def bfs(i):
    visited = [False for _ in range(n + 1)]
    que = deque([i])
    result2.append(i)
    visited[i] = True
    while que:
        i = que.popleft()
        for j in range(1, n+1):
            if graph[i][j] and not visited[i]:
                result2.append(i)
                visited[i] = True
                que.append(i)

dfs(s)
print(*result1)
bfs(s)
print(*result2)
