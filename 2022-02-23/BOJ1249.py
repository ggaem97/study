from collections import deque
import sys
sys.stdin = open('1249.txt', 'r')
move = [(1,0),(0,1),(-1,0),(0,-1)]


def bfs(x, y):
    deq = deque([(x, y)])
    while deq:
        x, y = deq.popleft()
        for dx, dy in move:
            nx, ny = dx + x, dy + y
            if 0 <= nx < n and 0 <= ny < n:
                # distance에 저장된 값보다 작다면
                if distance[x][y] + graph[nx][ny] < distance[nx][ny]:
                    deq.append((nx, ny))
                    distance[nx][ny] = distance[x][y] + graph[nx][ny]


for tc in range(1, int(input())+1):
    result = 0
    n = int(input())
    graph = [list(map(int, list(input()))) for _ in range(n)]
    distance = [[1e9]*n for _ in range(n)]
    distance[0][0] = 0
    for g in graph:
        print(g)
    bfs(0, 0)

    print(f'#{tc} {distance[n-1][n-1]}')