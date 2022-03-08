from collections import deque
import sys
sys.stdin = open('1249.txt', 'r')
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(x, y):
    que = deque([(x, y)])
    while que:
        i, j = que.popleft()
        for xx, yy in move:
            nx = xx + i
            ny = yy + j
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] + distance[i][j] < distance[nx][ny]:
                    distance[nx][ny] = distance[i][j] + graph[nx][ny]
                    que.append((nx, ny))


for tc in range(1, int(input())+1):
    n = int(input())
    graph = [list(map(int, input())) for _ in range(n)]
    distance = [[1e9]*n for _ in range(n)]
    distance[0][0] = 0
    for g in graph:
        print(g)
    print()
    bfs(0, 0)
    for d in distance:
        print(d)
    print(f'#{tc} {distance[n-1][n-1]}')