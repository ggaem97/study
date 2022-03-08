import sys
sys.stdin = open('1931.txt', 'r')
from collections import deque
n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]
# 종료 시간, 종료 시간이 같다면 시작 시간순으로 정렬
time.sort(key=lambda x:(x[1], x[0]))
deq = deque(time)
start, end = deq.popleft()
count = 1
while deq:
    next_start, next_end = deq.popleft()
    if end <= next_start:
        count += 1
        end = next_start
print(count)

