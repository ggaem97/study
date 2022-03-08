import sys
from collections import deque
sys.stdin = open('curiculum', 'r')
v = int(input())
times = [0]*(v+1)
mxCnt = [0] * (v + 1)
indegree = [0]*(v+1)
graph = [[] for _ in range(v+1)]

for i in range(1, v + 1):
    lst = list(map(int, input().split()))
    first = lst.pop(0)
    if first == -1:
        continue
    else:
        times[i] = first
    for data in lst:
        if data == -1:
            break
        else:
            indegree[i] += 1
            graph[data].append(i)
print('ind', indegree)

for i in range(v+1):
    mxCnt[i] = times[i]

def topology_sort():
    edges = deque()
    for i in range(1, v+1):
        if indegree[i] == 0:
            edges.append(i)
    # pre = 0
    while edges:
        now = edges.popleft()
        # result.append(times[now] + pre)
        # pre = times[now]
        for i in graph[now]:
            mxCnt[i] = max(mxCnt[i], mxCnt[now] + times[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                edges.append(i)


topology_sort()
# print('ind', indegree)
print('times', times)
print('graph', graph)
print(mxCnt)

