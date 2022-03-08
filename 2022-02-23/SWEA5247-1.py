from collections import deque
import sys
sys.stdin = open('5247.txt', 'r')


def bfs(N, M):
    que = deque([(N, 0)])
    dic = dict()
    while que:
        now, count = que.popleft()
        # 해당 숫자를 이미 방문한 경우
        if dic.get(now, 0): continue
        # 방문하지 않는 숫자인 경우
        dic[now] = 1
        if now == M:
            return count
        count += 1
        if 0 < now - 1 <= 10**6:
            que.append((now-1, count))
        if 0 < now + 1 <= 10**6:
            que.append((now+1, count))
        if 0 < now * 2 <= 10**6:
            que.append((now*2, count))
        if 0 < now - 10 <= 10**6:
            que.append((now-10, count))


for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    s = set()
    result = bfs(n, m)
    print(f'#{tc} {result}')