from collections import deque
import sys
sys.stdin = open('1012.txt', 'r')
move = [(1,0),(0,1),(-1,0),(0,-1)]


def bfs(x, y):
    deq = deque([(x, y)])
    graph[x][y] = 0
    while deq:
        x, y = deq.popleft()
        for dx, dy in move:
            nx, ny = dx + x, dy + y
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    deq.append((nx, ny))
    return 1


for _ in range(1, int(input())+1):
    result = 0
    n, m, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                result += bfs(i, j)
    print(result)