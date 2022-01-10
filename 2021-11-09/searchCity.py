from collections import deque
import sys
n,m,k,x= map(int,sys.stdin.readline().split())
destination = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    destination[a].append(b)

distance = [-1]*(n+1)
distance[x]=0

deq=deque([x])
while deq:
    target = deq.popleft()
    for next_node in destination[target]:
        if distance[next_node] == -1:
            distance[next_node] = distance[target] + 1
            deq.append(next_node)
check = True
for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        check = False

if check:
    print(-1)