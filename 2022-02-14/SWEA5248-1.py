from collections import deque
import sys
sys.stdin = open('5248.txt', 'r')

for tc in range(1, int(input())+1):
    answer = 0
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    q = deque(data)
    dp = [0]*(n+1)
    remain = set()
    while q:
        a, b = q.popleft(), q.popleft()
        if a not in remain and b not in remain:
            answer += 1
        remain.add(a)
        remain.add(b)
    for num in range(1, n+1):
        if num not in remain:
            answer += 1
    print(f'#{tc} {answer}')