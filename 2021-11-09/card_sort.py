import sys
import heapq
sys.stdin = open('in.txt','r')
n = int(sys.stdin.readline())
cards = []
for _ in range(n):
    data = int(sys.stdin.readline())
    heapq.heappush(cards, data)

while len(cards)>=2:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    print('a,b',a,b)
    heapq.heappush(cards,a+b)
    print(cards)

print(cards[0])