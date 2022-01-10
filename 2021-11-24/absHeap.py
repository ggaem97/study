import sys
import heapq
sys.stdin = open('in.txt','r')

n = int(sys.stdin.readline())
h = []

for _ in range(n):
    data = int(sys.stdin.readline())
    if data != 0:
        heapq.heappush(h,(abs(data),data))
    else:
        if not h:
            print(0)
        else:
            print(heapq.heappop(h)[1])

