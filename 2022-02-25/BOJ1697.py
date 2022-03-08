from collections import deque
import sys

sys.stdin = open('1697.txt', 'r')
N, K = map(int, input().split())


def bfs(n, k):
    que = deque([(n, 0)])
    dic = {}
    while que:
        now, count = que.popleft()
        if dic.get(now, 0):
            continue
        dic[now] = 1
        if now == k:
            return count

        count += 1
        if 0 <= (now - 1) <= 100000:
            que.append((now - 1, count))
        if 0 <= (now + 1) <= 100000:
            que.append((now + 1, count))
        if 0 <= now * 2 <= 100000:
            que.append((now * 2, count))


print(bfs(N, K))
