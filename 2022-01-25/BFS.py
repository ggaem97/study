from collections import deque
import sys
sys.stdin = open('bfs.txt', 'r')
n, k = map(int, input().split())
visited = [False]* (n+1)
print(visited)
graph = [[] for _ in range(n+1)]
for _ in range(k):
    a = list(map(int, input().split()))
    graph[a[0]] = a[1:]
print(graph)


def bfs():
    global graph
    start = 1
    que = deque()
    que.append(start)

    while que:
        node = que.popleft()
        print(node, end=' ')
        for nextNode in graph[node]:
            if not visited[nextNode]:
                visited[nextNode] = True
                que.append(nextNode)


bfs()