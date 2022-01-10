import copy
import sys
# print(datetime.datetime.now())
# 2021-12-17 15:24:50.360380
sys.stdin = open('in.txt','r')
n, k = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# board = [[1,0,2],[0,0,0],[3,0,0]]
# print(board)
tmp = copy.deepcopy(board)
# tmp = [[0]*n]*n
# print(tmp)
# for i in range(n):
#     for j in range(n):
#         tmp[i][j] = board[i][j]
# print(tmp)
s,x,y = map(int, sys.stdin.readline().split())

def dfs(x,y,v):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<n and 0<=yy<n and tmp[xx][yy] == 0:
            tmp[xx][yy] = v
            # print(tmp)

for _ in range(s):
    for virus in range(1,k+1):
        for i in range(n):
            for j in range(n):
                if board[i][j] == virus:
                    dfs(i,j,virus)

print(tmp[x-1][y-1])
