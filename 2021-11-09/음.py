import sys
import heapq
n=int(sys.stdin.readline())

heap=[]
for _ in range(n):
    data = int(sys.stdin.readline())
    heapq.heappush(heap, data)

result=0

while len(heap)!=1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)

    sumVal = a+b
    result+=sumVal
    heapq.heappush(heap, sumVal)

print(result)