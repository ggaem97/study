import sys
from collections import deque
sys.stdin = open('a.txt', 'r')
m, n, k = map(int, input().split())
board = [[0]*n for _ in range(m)]

dX = [1,0,-1,0]
dY = [0,1,0,-1]


def bfs(yy, xx):
    count = 1
    queue = deque([])
    queue.append([yy, xx])
    board[yy][xx] = count
    while queue:
        print(queue)
        y, x = queue.popleft()
        for dx, dy in zip(dX, dY):
            nx = dx + x
            ny = dy + y
            if 0 <= nx < n and 0 <= ny < m and board[ny][nx] == 0:
                board[ny][nx] = 1
                queue.append([ny, nx])
                count += 1
    print()
    return count


# 직사각형 세팅하기
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            board[y][x] = 1


area = []
for i in range(m):
    for j in range(n):
        # '0'이라면 영역 구하기
        if board[i][j] == 0:
            area.append(bfs(i, j))


print(len(area))
for data in sorted(area):
    print(data, end=' ')