n = 3
k = 3
board = [[1,0,2],[0,0,0],[3,0,0]]
time = 2
x, y = 3,2

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def contagious(x, y):
    num = board[x][y]

    for m in range(4):
        xx = x + dx[m]
        yy = y + dy[m]




