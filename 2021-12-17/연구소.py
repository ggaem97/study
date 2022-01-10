import copy

n = 7
m = 7
board = [[2,0,0,0,1,1,0],
         [0,0,1,0,1,2,0],
         [0,1,1,0,1,0,0],
         [0,1,0,0,0,0,0],
         [0,0,0,0,0,1,1],
         [0,1,0,0,0,0,0],
         [0,1,0,0,0,0,0]]
tmpBoard = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]
            ,[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
result = 0
def virus(x,y):
    dx = [0,1,-1,0]
    dy = [-1,0,0,1]
    tmpBoard[x][y] = 2
    for i in range(4):
        xx = dx[i] + x
        yy = dy[i] + y
        if 0<=xx<7 and 0<=yy<7 and tmpBoard[xx][yy] == 0:
            virus(xx,yy)

def get_score():
    sum = 0
    for i in range(n):
        for j in range(m):
           if tmpBoard[i][j] == 0:
               sum += 1
    return sum

def dfs(cnt):
    global result

    if cnt == 3:
        # 반드시 이런식으로 할당해야
        # deepcopy 안됨 [:] 안됨
        for i in range(n):
            for j in range(m):
                tmpBoard[i][j] = board[i][j]

        for i in range(n):
            for j in range(m):
                if tmpBoard[i][j] == 2:
                    virus(i,j)
        # print('tmpBoard',tmpBoard)
        result = max(result, get_score())
        return

    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1
                cnt += 1
                dfs(cnt)
                cnt -= 1
                board[i][j] = 0

dfs(0)
print(result)


