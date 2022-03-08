from collections import deque
import sys
sys.stdin = open('1249.txt', 'r')
move = [(1,0),(0,1),(-1,0),(0,-1)]


def bfs(x, y):
    deq = deque([(x,y)])
    while deq:
        x, y = deq.popleft()
        for dx, dy in move:
            nx = dx + x
            ny = dy + y
            if 0 <= nx < n and 0 <= ny < n:
                # 만약 더 짧은 거리가 있다면 최소 거리로 갱신
                if distance[x][y] + graph[nx][ny] < distance[nx][ny]:
                    distance[nx][ny] = graph[nx][ny] + distance[x][y]
                    deq.append((nx, ny))


for tc in range(1, int(input())+1):
    n = int(input())
    graph = [list(map(int, input())) for _ in range(n)]
    distance = [[1e9]*n for _ in range(n)]
    distance[0][0] = graph[0][0]
    bfs(0, 0)
    for dd in distance:
        print(dd)
    print()
    print(f'#{tc} {distance[n-1][n-1]}')