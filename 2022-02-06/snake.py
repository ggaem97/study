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
from collections import deque

x, y = 0, 0
# while True:
def game():
    print('진행중...')
    # 뱀의 몸뚱아리 정보 저장
    que = deque([(x, y)])
    board[x][y] = 2
    while True:
        for bb in board:
            print(bb)
        print()
        # 동쪽으로만 움직인다고 해보자
        nx, ny = x + dx[0], y + dy[0]
        if 0 > nx or nx >= n or 0 > ny or ny >= n:
            print('벽에 닿아서 종료합니다.')
            break
        if board[nx][ny] == 2:
            print('자기 몸에 닿아서 죽었습니다.')
            break
        # 사과가 있는 경우
        if board[nx][ny] != 1:
            xx, yy = que.popleft()
            board[xx][yy] = 0
        # 맨마지막 꼬리를 제거
        # board[nx-dx[0]][ny-dy[0]] = 0
        que.append((nx, ny))
        board[nx][ny] = 2

print(game())