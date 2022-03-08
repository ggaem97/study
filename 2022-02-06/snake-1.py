# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def turn(d, check):
    print('turned!')
    # 왼쪽으로 회전
    if d == 'L':
        if check == 0:
            return 3
        return check - 1
    # 오른쪽으로 회전
    else:
        if check == 3:
            return 0
        return check + 1


n = 6
board = [[0] * n for _ in range(6)]
# 사과 세팅
board[2][3] = 1
board[0][3] = 1
board[4][1] = 1
board[2][5] = 1
board[4][4] = 1
board[0][1] = 1
for bb in board:
    print(bb)
print()


def dfs(x, y):
    global snake
    print('x,y', x,y)
    # 동쪽으로만 움직인다고 가정
    nx, ny = x + dx[0], y + dy[0]
    if 0 > nx or nx >= n or 0 > ny or ny >= n:
        print('벽에 닿아서 종료합니다..')
        return
    # 사과가 없다면
    if board[nx][ny] != 1:
        # 마지막 꼬리 제거 > 어떻게 제거하지...???????????
        xx, yy = snake.pop(0)
        board[xx][yy] = 0
        dfs(nx, ny)
    # 뱀의 머리
    board[nx][ny] = 2
    snake.append((nx, ny))
    for bb in board:
        print(bb)
    print()
    dfs(nx, ny)
    # board[nx][ny] = 0

snake = [(0, 0)]
board[0][0] = 2
print('start')
dfs(0, 0)
print(snake)