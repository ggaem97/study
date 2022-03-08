from collections import deque
import sys
sys.stdin = open('7576.txt', 'r')
move = [(1,0), (0,1), (-1,0), (0,-1)]


def bfs(tomato):
    # print(que)
    time = 0
    deq = deque(tomato)
    while deq:
        x, y, t = deq.popleft()
        time = t
        # print('익은 x, y t', x, y, t)
        for dx, dy in move:
            nx, ny = dx + x, dy + y
            if 0 <= nx < n and 0 <= ny < m:
                # 토마토가 아직 익지 않았다면
                if box[nx][ny] == 0:
                    # 토마토를 익혀라!!
                    box[nx][ny] = 1
                    deq.append((nx, ny, t+1))
    return time


m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
result = 0
already = []
for i in range(n):
    for j in range(m):
        # 익은 토마토의 위치 저장하기
        if box[i][j] == 1:
            already.append((i, j, 0))
result = bfs(already)
# 익지 않은 토마토가 있다면 -1 리턴
for i in range(n):
    if 0 in box[i]:
        result = -1
        break
print(result)