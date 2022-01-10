import sys

sys.stdin = open('in4.txt', 'r')
n, m = map(int, input().split())
x, y, direction = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
for b in board:
    print(b)
d = [[0] * n] * m
d[x][y]=1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 육지의 개수 카운트
# 처음 좌표는 반드시 육지이므로 카운트 1로 초기화
cnt = 1
turnTimes = 0


def turnLeft():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


while True:
    # 왼쪽으로 회전
    turnLeft()
    # 회전 후 한칸 이동
    xx = x + dx[direction]
    yy = y + dy[direction]
    # 왼쪽 방향에 가보지 않은 칸 존재하는 경우
    # (사방이 바다여서 range 처리 안해줘도 됨)
    if board[xx][yy] == 0 and d[xx][yy] == 0:
        # print('xx,yy', xx,yy)
        d[xx][yy] = 1
        x = xx
        y = yy
        cnt += 1
        turnTimes = 0
        continue
    # 가보지 않은 칸이 존재하지 않는 경우
    else:
        turnTimes += 1

    if turnTimes == 4:
        xx = x - dx[direction]
        yy = y - dy[direction]
        if board[xx][yy] == 0:
            x = xx
            y = yy
        else:
            break
        turnTimes = 0
print(d)
print(cnt)