import sys
n,m = map(int, sys.stdin.readline().split())
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
tmp = [[0]*m for _ in range(n)]
# tmp = [[] for _ in range(n)]
# 바이러스 전파
def virus(x,y):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0<=xx<n and 0<=yy<m and tmp[xx][yy]==0:
            tmp[xx][yy]=2
            virus(xx,yy)

#안전영역 개수 구하기
def Count():
    cnt=0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                cnt+=1
    return cnt

def DFS(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                tmp[i][j] = lab[i][j]
                # tmp[i].append(lab[i][j])

        for i in range(n):
            for j in range(m):
                if tmp[i][j]==2:
                    virus(i,j)
        result = max(result, Count())
        return
    else:
        for i in range(n):
            for j in range(m):
                if lab[i][j] == 0:
                    lab[i][j]=1
                    count+=1
                    DFS(count)
                    lab[i][j]=0
                    count-=1
result=0
DFS(0)
print(result)
