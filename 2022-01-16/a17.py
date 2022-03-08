from collections import deque
import sys
# input = sys.stdin.readline
sys.stdin = open('a.txt', 'r')
n, k = map(int, input().split())
graph = []
data = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

data.sort()
q = deque(data)

time, a, b = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while q:
    virus, t, x, y = q.popleft()
    if t == time:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and graph[nx][ny] == 0:
            graph[nx][ny] = virus
            q.append((virus, t+1, nx, ny))

print(graph[a-1][b-1])