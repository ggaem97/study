import sys
sys.stdin = open('boom.txt', 'r')
r,c,time = map(int, input().split())
board = [list(map(str, input())) for _ in range(r)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]


def findBomb():
    bombBox = []
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'O':
                bombBox.append((i,j))
    return bombBox


def bomb():
    # 이전에 설치된 폭탄
    bombBox = findBomb()
    # 폭탄 설치
    for x in range(r):
        for y in range(c):
            if board[x][y] == '.':
                board[x][y] = 'O'
    # 이전에 설치된 폭탄 터트리기
    for x, y in bombBox:
        board[x][y] = '.'
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            if 0 <= nx < r and 0 <= ny < c:
                board[nx][ny] = '.'


if time % 2 == 0:
    for i in range(r):
        print('O'*c)
else:
    for i in range(3, time+1):
        # 홀수번째
        if i%2 == 1:
            bomb()
        if i == time:
            for k in range(r):
                print(''.join(board[k]))

