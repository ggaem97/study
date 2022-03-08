# snake
import sys
sys.stdin = open('snake2', 'r')
n = int(input())
board = [[0]*(n+1) for i in range(n+1)]
k = int(input())
# board[0][0] = 2
direction = 1
positionBox = []
for i in range(k):
    x, y = map(int, input().split())
    # 사과가 있는 경우 1로 처리
    board[x-1][y-1] = 1
#     북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 회전 함수
def switchPosition(s):
    global direction
    # 오른쪽으로 90도 회전
    if s == 'D':
        p += 1
        if p == 4:
            p = 0
    else:
        p -= 1
        if p == -1:
            p = 3

m = int(input())
for i in range(m):
    t, position = map(str, input().split())
    time = int(t)
    positionBox.append((t, position))

positionBox.sort(key=lambda x: int(x[0]))
print(positionBox)
# 게임 시작
def game():
    print("let's start!!  ")
    x, y = 0, 0
    t = 0
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()

    while True:
        # 꼬리 해결 못함
        print('x:',x,'y:',y)
        print('t:',t)
        if positionBox:
            if t == int(positionBox[0][0]):
                switchPosition(positionBox[0][1])
                positionBox.pop(0)
                print('box''s element popped!')
        board[x][y] = 2
        x = x + dx[direction]
        y = y + dy[direction]
        if board[x][y] == 2:
            break
        if x < 0 or x >= n or y < 0 or y >= n:
            break
        if board[x][y] == 1:
            pass
        else:
            board[x - dx[direction]][y - dy[direction]] = 0

        t += 1
    print()
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()


    return t


mxCnt = game()
print(mxCnt + 1)
