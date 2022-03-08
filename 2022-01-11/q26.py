import heapq
import sys
sys.stdin = open('q26', 'r')
n = int(sys.stdin.readline().strip())
h = []
answer = 0
for _ in range(n):
    data = int(sys.stdin.readline().strip())
    heapq.heappush(h, data)
if len(h) == 1:
    answer = heapq.heappop(h)

while len(h) != 1:
    first = heapq.heappop(h)
    last = heapq.heappop(h)
    summary = first+last
    answer += summary
    heapq.heappush(h, summary)

print(answer)