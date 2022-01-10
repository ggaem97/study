import sys
import heapq

sys.stdin = open('a.txt','r')

n,m = map(int, input().split())
start = int(input())
INF = 1e9
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for i in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    distance[start] = 0
    h = []
    heapq.heappush(h,(0, start))
    while h:
        dist, now = heapq.heappop(h)
        # 현재 노드가 이미 처리된적 있다면 넘어감
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(h,(cost,i[0]))

dijkstra(start)

for i in range(n+1):
    if distance[i] == 'INF':
        print('INFINITE')
    else:
        print(distance[i])