from collections import deque
import sys

sys.stdin = open('위상정렬.txt', 'r')
v, e = map(int, input().split())

indegrees = [0]*(v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegrees[b] += 1

print(graph)
print(indegrees)

def topology_sort():
    result = []
    q = deque()

    # 진입 차수가 0인 노드 큐에 삽입
    for i in range(1, v+1):
        if indegrees[i] == 0:
            q.append(i)
    # print(q)
    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegrees[i] -= 1

            if indegrees[i] == 0:
                q.append(i)

    for data in result:
        print(data, end=' ')

topology_sort()