import datetime
import copy
from itertools import combinations
# print(datetime.datetime.now())
# 2021-12-17 12:23:23.667703

n = 7
m = 7
board = [[2,0,0,0,1,1,0],
         [0,0,1,0,1,2,0],
         [0,1,1,0,1,0,0],
         [0,1,0,0,0,0,0],
         [0,0,0,0,0,1,1],
         [0,1,0,0,0,0,0],
         [0,1,0,0,0,0,0]]
tmpBoard = []
def dfs(x,y):
    dx = [0,1,-1,0]
    dy = [-1,0,0,1]
    tmpBoard[x][y] = 2
    for i in range(4):
        xx = dx[i] + x
        yy = dy[i] + y
        if 0<=xx<7 and 0<=yy<7 and tmpBoard[xx][yy] == 0:
            dfs(xx,yy)
zeroIdxs = []
for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            zeroIdxs.append((i,j))


idxBox = list(combinations(zeroIdxs,3))
safeZone = []
for box in idxBox:
    tmpBoard = copy.deepcopy(board)
    # print('tmpBoard',tmpBoard)
    for pair in box:
        x,y = pair
        tmpBoard[x][y] = 1
    # print('벽설치 후 ', tmpBoard)
    for i in range(m):
        for j in range(n):
            if tmpBoard[i][j] == 2:
                dfs(i, j)
    # print('result tmpBoard', tmpBoard)
    sum = 0
    for i in range(m):
        for j in range(n):
           if tmpBoard[i][j] == 0:
               sum += 1

    if sum != 0:
        safeZone.append(sum)
    # print()
print(max(safeZone))

