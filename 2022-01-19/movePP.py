from collections import deque
import sys
sys.stdin = open('in3.txt', 'r')

n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]


def process(i, j, index):
    united = []
    united.append((i,j))
    count = 1
    summary = board[i][j]
    q = deque([(i,j)])
    union[i][j] = index
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<n and union[nx][ny] == -1:
                if l <= abs(board[nx][ny] - board[x][y]) <= r:
                    summary += board[nx][ny]
                    count += 1
                    q.append((nx,ny))
                    united.append((nx,ny))
                    union[nx][ny] = index

    for x, y in united:
        board[x][y] = summary//count


total_cnt = 0
while True:
    union = [[-1]*n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i,j, index)
                index += 1
    if index == n*n:
        break
    total_cnt += 1
print(total_cnt)