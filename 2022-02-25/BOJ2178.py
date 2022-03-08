from collections import deque
import sys
sys.stdin = open('2178.txt', 'r')
n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]
print(graph)
move = [(1,0),(0,1),(-1,0),(0,-1)]


def bfs(i, j):
    deq = deque([(i, j)])
    while deq:
        x, y = deq.popleft()
        for dx, dy in move:
            nx, ny = dx + x, dy + y
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    deq.append((nx, ny))


bfs(0, 0)
print(graph[n-1][m-1])