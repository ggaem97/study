from collections import deque
import sys
sys.stdin = open('in3.txt', 'r')

n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]


def process(x,y, index):
    # (x,y)의 위치 그리고 연결된 나라 정보를 담음
    united = []
    united.append((x,y))
    # 현재 연합 번호 할당
    union[x][y] = index
    summary = board[x][y]
    count = 1
    q = deque()
    q.append((x,y))
    while q:
        # print('x,y',x,y)
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<n and 0<=ny<n and union[nx][ny] == -1:
                if l <= abs(board[nx][ny] - board[x][y]) <= r:
                    # 연합에 추가
                    q.append((nx,ny))
                    union[nx][ny] = index
                    summary += board[nx][ny]
                    count += 1
                    united.append((nx,ny))
    print('union')
    for i in range(n):
        print(union[i])
    # 인구 분배
    for i, j in united:
        board[i][j] = summary//count
    print('board')
    for i in range(n):
        print(board[i])
    return count


total_count = 0
while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i,j, index)
                index += 1
    if index == n*n:
        break
    total_count += 1

print('board')
for i in range(n):
    print(board[i])
print('union')
for i in range(n):
    print(union[i])
print(total_count)

