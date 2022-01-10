from collections import deque
import datetime
# print(datetime.datetime.now())
# 2021-12-17 11:10:21.102910
n = 4
m = 4
k = 1
x = 1

graph = [[],
         [2,3],
         [3,4],
         [],
         []]

distance = [0] *(n+1)
startNode = x

deq = deque([startNode])
while deq:
    # print('deq',deq)
    node = deq.popleft()
    for nextNode in graph[node]:
        if distance[nextNode] == 0:
            distance[nextNode] = distance[node] + 1
            deq.append(nextNode)
        # if cnt[nextNode] != 0:
        #     cnt[nextNode] = min(cnt[nextNode], cnt[node] + 1)
        # else:
        #     cnt[nextNode] = cnt[node] + 1
# print(cnt)

if k not in distance:
    print(-1)
else:
    for i in range(1,n+1):
        if distance[i] == k:
            print(i)


# stack = [startNode]
# while stack:
#     for secondNode in graph[startNode]:
#         visited[secondNode] = True
#         stack.append(secondNode)
#         cnt[secondNode] += 1
#         for node in graph[secondNode]:
#             if not visited[node]:
#                 stack.append(node)
#                 visited[node] = True
#         else:
#             stack.pop()
# def dfs(node):
#     visited[node] = True
#
#     for nextNode in graph[node]:
#         if not visited[nextNode]:
#             cnt[node] += 1
#             dfs(nextNode)
#
#
# dfs(startNode)
# print(cnt)

