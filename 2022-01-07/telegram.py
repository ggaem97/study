import sys
import heapq
sys.stdin = open('in2.txt', 'r')

n, m, c = map(int, input().split())
INF = 1e9
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
distance[c] = 0
for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

print(graph)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        # i[0]: node i[1]: distance
        for i in graph[now]:
            # cost = i[1] + distance[now]
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (distance[i[0]], i[0]))

dijkstra(c)
print(distance)
place = 0
time = 0
for cost in distance:
    if cost != INF and cost != 0:
        place += 1
        time = max(time, cost)

print(place, time)