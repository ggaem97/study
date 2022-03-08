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
deq = deque(jewel)
heap = []
print('jewel', jewel)
print('c', c)
# 가방에 담을 수 있는 보석을 찾아보자
for i in range(k):
    while deq:
        # 가방이 담을 수 없는 보석이 등장했다면
        if heap and c[i] < deq[0][0]:
            data = -heapq.heappop(heap)
            print(data)
            result += data
            break
        # 가방이 담을 수 있는 보석인 경우
        m, v = deq.popleft()
        heapq.heappush(heap, -v)

print(result)