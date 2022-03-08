from collections import deque
import sys
sys.stdin = open('5247.txt', 'r')


def bfs(N, M):
    deq = deque([(N, 0)])
    visited = set()
    while deq:
        now, count = deq.popleft()
        print('now, count', now, count)
        if now in visited:
            continue
        visited.add(now)
        if now == M:
            return count
        count += 1
        if 0 < now - 1 <= 1000000:
            deq.append((now-1, count))
        if 0 < now + 1 <= 1000000:
            deq.append((now+1, count))
        if 0 < now * 2 <= 1000000:
            deq.append((now*2, count))
        if 0 < now - 10 <= 1000000:
            deq.append((now-10, count))


for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    result = bfs(n, m)
    print(f'#{tc} {result}')