import sys

sys.stdin = open('in.txt', 'r')
start = 1
n, m = map(int, input().split())
INF = 1e9
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

x, k = map(int, input().split())

distance = graph[1][k] + graph[k][x]

# for i in range(n+1):
#     for j in range(n+1):
#         if graph[i][j] == INF:
#             print(-1, end = ' ')
#         else:
#             print(graph[i][j], end=' ')
#     print(' ')

if distance >= INF:
    print(-1)
else:
    print(distance)