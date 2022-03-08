import heapq
import sys
sys.stdin = open('1202.txt', 'r')
N, K = map(int, sys.stdin.readline().split())

jewelryList = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
bagList = [int(sys.stdin.readline()) for _ in range(K)]
jewelryList.sort()
bagList.sort()

result = 0
temp = []
print(jewelryList)
print(bagList)
for bagWeight in bagList:
    while jewelryList and bagWeight >= jewelryList[0][0]:
        heapq.heappush(temp, -jewelryList[0][1])  # Max heap
        heapq.heappop(jewelryList)

    if temp:
        data = heapq.heappop(temp)
        result += data
    elif not jewelryList:
        break

print(-result)