from collections import deque
n,m = 5,6
board = [[1,0,1,0,1,0],[1,1,1,1,1,1],[0,0,0,0,0,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
def bfs(x,y):
    deq = deque()
    deq.append((x,y))
    while deq:
        x, y = deq.popleft()
        for i in range(4):
            xx = dx[i] + x
            yy = dy[i] + y
            if 0<=xx<=4 and 0<=yy<=5 and board[xx][yy] == 1:
                deq.append((xx,yy))
                board[xx][yy] = 1 + board[x][y]

for i in range(5):
    for j in range(6):
        if board[i][j] == 1:
            bfs(i,j)

print(board)
print(board[4][5])