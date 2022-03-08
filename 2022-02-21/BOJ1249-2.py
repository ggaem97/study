import heapq
import sys
move = [(1,0),(0,1),(-1,0),(0,-1)]
sys.stdin = open('1249.txt', 'r')

def dijkstra(d, x, y):
    queue = []
    heapq.heappush(queue, (d, x, y))
    while queue:
        d, x, y = heapq.heappop(queue)
        for dx, dy in move:
            nx = dx + x
            ny = dy + y
            if 0 <= nx < n and 0 <= ny < n:
                # 만약 더 짧은 거리가 있다면 최소 거리로 갱신
                if distance[nx][ny] > d + graph[x][y]:
                    distance[nx][ny] = d + graph[x][y]
                    heapq.heappush(queue, (distance[nx][ny], nx, ny))


for tc in range(1, int(input())+1):
    n = int(input())
    graph = [list(map(int, input())) for _ in range(n)]
    distance = [[1e9]*n for _ in range(n)]
    distance[0][0] = graph[0][0]
    dijkstra(0, 0, 0)
    print(f'#{tc} {distance[n-1][n-1]}')