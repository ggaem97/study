import sys
import heapq
sys.stdin = open('in.txt','r')

n = int(sys.stdin.readline())
h = []
for _ in range(n):
    data = int(sys.stdin.readline())
    if data !=0:
        heapq.heappush(h,data)
    else:
        if h:
            print(heapq.heappop(h))
        else:
            print(0)

