import sys
sys.stdin = open('marble.txt', 'r')
from collections import deque
n,m = map(int,input().split())
grid,visit = [],set()
redI,redJ,blueI,blueJ = -1,-1,-1,-1
for i in range(n):
    row = input()
    for j in range(m):
        if row[j]=='R': redI,redJ=i,j
        if row[j]=='B': blueI,blueJ=i,j
    grid.append(list(row))

print(redI,redJ,blueI,blueJ)


def move(i, j, di, dj, redi, redj, bluei, bluej):
    while True:
        if grid[i+di][j+dj]=='#' or (i+di,j+dj) in ((redi,redj),(bluei,bluej)):
            return (i,j)
        if grid[i+di][j+dj]=='O':
            return (-1,-1)
        i+=di
        j+=dj


que=deque()
que.append((redI, redJ, blueI, blueJ))
visit.add((redI,redJ,blueI,blueJ))
for MOVE in range(10):
    for _ in range(len(que)):
        redI,redJ,blueI,blueJ = que.popleft()
        for di,dj in (-1,0),(1,0),(0,-1),(0,1):
            ri,rj=move(redI,redJ,di,dj,redI,redJ,blueI,blueJ)
            bi,bj=move(blueI,blueJ,di,dj,ri,rj,blueI,blueJ)
            ri,rj=move(ri,rj,di,dj,ri,rj,bi,bj)
            if bi == -1:
                continue
            if ri == -1:
                print(MOVE+1)
                exit()
            if (ri,rj,bi,bj) in visit:
                continue
            visit.add((ri,rj,bi,bj))
            que.append((ri, rj, bi, bj))
print(-1)