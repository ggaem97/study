from collections import deque
import sys

dx = [1,0,-1,0]
dy = [0,-1,0,1]

def bfs(x,y):
    que = deque([(x,y)])
    while que:
        x,y = que.popleft()
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if xx<0 or xx>N-1 or yy<0 or yy>M-1:
                continue
            if graph[xx][yy] == 0:
                continue
            if graph[xx][yy] == 1:
                graph[xx][yy]=graph[x][y] + 1
                que.append((xx,yy))
    return graph[N-1][M-1]

N, M = map(int, sys.stdin.readline().strip().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip())))


result = bfs(0,0)
print(result)