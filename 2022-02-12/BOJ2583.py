# dfs나 bfs로 풀이하면 좋겠다
import sys
sys.stdin = open('2583.txt', 'r')
m, n, k = map(int, input().split())
board = [[0]*n for _ in range(m)]
print(board)
position = [(1,0),(0,1),(-1,0),(0,-1)]


def dfs(x, y, count):
    board[x][y] = 1

    for dx, dy in position:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < m and 0 <= ny < n:
            if board[nx][ny] == 0:
                print('counter is', count)
                print(nx, ny)
                dfs(nx, ny, count+1)


for _ in range(k):
    a, b, c, d = map(int, input().split())
    print(a, b, c, d)
    for x in range(b, d):
        for y in range(a, c):
            board[m-1-x][y] = 1
for bb in board:
    print(bb)
part = 0
cntLst = []
for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            part += 1
            cnt = dfs(i,j,1)
            cntLst.append(cnt)
print(part)
for c in cntLst:
    print(c, end=' ')