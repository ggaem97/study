# 다익스트라 알고리즘 : 우선순위 큐 사용
import sys
import heapq
sys.stdin = open('1916', 'r')


def dijkstra():
    global start
    que = []
    heapq.heappush(que, (0, start))
    costLst[start] = 0
    while que:
        # 거리가 가장 작은 노드 꺼내기
        d, node = heapq.heappop(que)
        print('거리',d,' 노드',node)
        if costLst[node] < d:
            continue
        for i in graph[node]:
            nextNode, cost = i[0], i[1]
            weight = d + cost
            if weight < costLst[nextNode]:
                costLst[nextNode] = weight
                heapq.heappush(que, (weight, nextNode))
        print(que)
        print(costLst)
    print('costLst', costLst)


n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
costLst = [1e9 for i in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
for i in range(1, n):
        for j in graph[i]:
            print('node:',i, 'nextNode:',j[0], 'distance:',j[1])
start, end = map(int, input().split())
print(start, end)
dijkstra()
print(costLst[end])