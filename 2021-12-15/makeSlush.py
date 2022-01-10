dx = [0,1,-1,0]
dy = [1,0,0,-1]

board = [[0,0,1,1,0],[0,0,0,1,1],[1,1,1,1,1],[0,0,0,0,0]]

def dfs(xx,yy):
    board[xx][yy] = 1
    for i in range(4):
        x = dx[i] + xx
        y = dy[i] + yy
        if 0<=x<=3 and 0<=y<=4 and board[x][y] == 0:
            dfs(x,y)
cnt = 0
for i in range(4):
    for j in range(5):
        if board[i][j] == 0:
            dfs(i,j)
            cnt+=1
print(board)
print(cnt)