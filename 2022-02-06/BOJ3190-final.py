from collections import deque
import sys
# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def turn(check, d):
    # print('turned!')
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


sys.stdin = open('3190.txt', 'r')
n = int(input())
board = [[0]*n for _ in range(n)]
k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1
l = int(input())
table = [(input().split()) for _ in range(l)]
time = 1
# 뱀의 몸뚱아리 정보 때문에 bfs로 시작
def game():
    global time
    # print('game start')
    nx, ny = 0, 0
    que = deque([(nx, ny)])
    direction = 0
    board[nx][ny] = 2
    while True:
        nx, ny = nx + dx[direction], ny+dy[direction]
        if 0 > nx or nx >= n or 0 > ny or ny >= n:
            # print('벽에 닿아서 종료합니다')
            break
        if board[nx][ny] == 2:
            # print('뱀이 지 몸에 닿아 종료합니다')
            break
        # 사과 만나는 경우 아니면 꼬리 제거
        if board[nx][ny] != 1:
            xx, yy = que.popleft()
            board[xx][yy] = 0
        # 머리 붙이기
        board[nx][ny] = 2
        que.append((nx, ny))
        if table:
            if int(table[0][0]) == time:
                # print('방향을 회전해야 합니다...')
                t, d = table.pop(0)
                direction = turn(direction, d)
        time += 1

game()
print(time)