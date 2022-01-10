import sys
import heapq

sys.stdin = open('a.txt','r')

n,m = map(int, input().split())
start = int(input())
INF = 1e9
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
visited = [False]*(n+1)

for i in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

print(graph)

def dijkstra(start):
    distance[start] = 0
    h = []
    heapq.heappush(h,(0, start))
    while h:
        print('h>', h)
        dist, now = heapq.heappop(h)
        if start != now and visited[now] == True:
            continue
        print('distance =',distance)
        print('dist>',dist,'now>',now)
        visited[now] = True
        for i in graph[now]:
            # if distance[now] < INF:
            #     continue
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
            heapq.heappush(h,(distance[i[0]],i[0]))
        print('visited>',visited)
        print('************')

dijkstra(start)

for i in range(n+1):
    if distance[i] == 'INF':
        print('INFINITE')
    else:
        print(distance[i])