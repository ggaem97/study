import heapq
import sys
sys.stdin = open('1753.txt', 'r')


def dijkstra(start):
    queue = []
    distance[start] = 0
    heapq.heappush(queue, (0, start))

    while queue:
        cost, now = heapq.heappop(queue)
        # 저장된 비용이 현재 비용보다 적다면 무시
        if cost > distance[now]:
            continue
        for next_cost, next_node in graph[now]:
            next_cost += cost
            if next_cost < distance[next_node]:
                distance[next_node] = next_cost
                heapq.heappush(queue, (next_cost, next_node))


v, e = map(int, input().split())
s = int(input())
graph = [[] for _ in range(v+1)]
distance = [1e9 for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    # (비용, 도착노드) 저장
    graph[a].append((c, b))
dijkstra(s)
for i in range(1, v+1):
    if distance[i] == 1e9:
        print('INF')
    else:
        print(distance[i])