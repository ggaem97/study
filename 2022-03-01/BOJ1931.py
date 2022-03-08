import sys
from collections import deque
sys.stdin = open('1931.txt', 'r')

n = int(input())
time = [list(map(int,input().split())) for _ in range(n)]
# 최대한 빨리 끝내는 순으로 정렬
time.sort(key=lambda x:(x[1],x[0]))
deq = deque(time)
start, end = deq.popleft()
cnt = 1
while deq:
    if deq[0][0] >= end:
        cnt += 1
        start, end = deq.popleft()
    else:
        deq.popleft()
print(cnt)
