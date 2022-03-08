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
    for _ in range(m):
        a, b = q.popleft(), q.popleft()
        remain.add(a)
        remain.add(b)
        if dp[a] == 0 and dp[b] == 0:
            answer += 1
        dp[a], dp[b] = 1, 1
    for i in range(1, n+1):
        if i not in remain:
            answer += 1
    print(f'#{tc} {answer}')