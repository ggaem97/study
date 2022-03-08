import heapq
from collections import deque
import sys
sys.stdin = open('1202.txt', 'r')

# 보석의 개수, 가방의 개수
n, k = map(int, input().split())
jewel = []
for _ in range(n):
    # 보석의 무게, 보석의 가격
    m, v = map(int, input().split())
    jewel.append([m, v])
# 가방에 담을 수 있는 최대 무게
c = sorted([int(input()) for _ in range(k)])
jewel.sort(key=lambda x:(x[0], -x[1]))
result = 0
# deq = deque(jewel)
# 가방에 담을 수 있는 보석을 찾아보자
heap = []
print(jewel)
print(c)
for i in range(k):
    while jewel and c[i] >= jewel[0][0]:
        heapq.heappush(heap, -jewel[0][1])
        heapq.heappop(jewel)
    if heap:
        data = heapq.heappop(heap)
        print('data', data)
        result += data
    elif not jewel:
        break

print(-result)