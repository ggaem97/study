import sys
sys.stdin = open('in4.txt', 'r')

n = int(input())
v = int(input())
INF = 1e9
graph = [[INF]*(n) for _ in range(n)]
distance = [[0]*n for _ in range(n)]

for _ in range(v):
    a, b, cost = map(int, input().split())
    graph[a-1][b-1] = min(cost, graph[a-1][b-1])

for i in range(n):
    for j in range(n):
        distance[i][j] = graph[i][j]

for k in range(n):
    for a in range(n):
        for b in range(n):
            if a == b:
                distance[a][b] = 0
            else:
                if a == 3 and b == 2:
                    print(distance[a][b], graph[a][k]+graph[k][b])
                distance[a][b] = min(distance[a][b], graph[a][k]+graph[k][b])

for i in range(n):
    for j in range(n):
        if distance[i][j] == 1e9:
            print(0, end=' ')
        else:
            print(distance[i][j], end=' ')
    print()

