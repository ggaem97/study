import sys
input = sys.stdin.readline
# sys.stdin = open('a.txt', 'r')
n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
time, x, y = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def contagious(tmp, x, y):
    num = tmp[x][y]

    for m in range(4):
        xx = x + dx[m]
        yy = y + dy[m]
        if 0 <= xx < n and 0 <= yy < n and tmp[xx][yy] == 0:
            tmp[xx][yy] = num


tmp = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        tmp[i][j] = board[i][j]
t = 0
while True:
    t += 1
    if t > time:
        break
    # print('time is..', t,'->',t+1)
    for num in range(1, k + 1):
        for i in range(n):
            for j in range(n):
                if board[i][j] == num:
                    contagious(tmp, i, j)

    for i in range(n):
        for j in range(n):
            board[i][j] = tmp[i][j]

print(board[x - 1][y - 1])
