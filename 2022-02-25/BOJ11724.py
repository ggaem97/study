import sys
sys.stdin = open('11724.txt', 'r')
# 정점, 간선의 개수
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]


def find(x, parent):
    if parent[x] != x:
        return find(parent[x], parent)
    return x


def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [i for i in range(n+1)]
for a in range(1, n+1):
    for b in graph[a]:
        union(a, b, parent)
result = set()
for i in range(1, n+1):
    result.add(parent[i])
print(len(result))