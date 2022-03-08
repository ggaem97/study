import sys
sys.stdin = open('1916', 'r')

n = int(input())
m = int(input())
INF = 1e9
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())
# 아직 방문하지 않고 거리가 가장 짧은 노드 구하기
def get_smallest_node():
    min_val = INF
    idx = 0
    for i in range(1, n+1):
        if distance[i] < min_val and not visited[i]:
            min_val = distance[i]
            idx = i
    return idx


def dijkstra():
    global start
    # 목적지 노드가 자기 자신(출발 노드)인 경우 거리는 0
    distance[start] = 0
    # 자기 자신 방문 처리
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 출발지 노드를 제외한 n-1개의 노드에 대해 반복
    for i in range(n-1):
        now = get_smallest_node()
        # 방문 처리
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra()
print(distance[end])