from itertools import combinations
from collections import deque

computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
deq = deque([(0,0)])
answer = 0
n = len(computers)
for i in range(n):
    computers[i][i] = 0

deq = deque([(0,0)])
while deq:
    print('deq', deq)
    node,cnt = deq.popleft()
    for nextNode in computers[node]:
        if nextNode > node and nextNode == 1:
            deq.append((nextNode, cnt+1))
    answer = max(answer, cnt)
print(answer)
# while deq:
#     print(deq)
#     s,l = deq.popleft()
#     if l>len(numbers):
#         break
#     if l==len(numbers) and target == s:
#         cnt +=1
#     else:
#         deq.append((s+numbers[l-1],l+1))
#         deq.append((s-numbers[l-1],l+1))

# print(cnt)