import sys
sys.stdin = open('watch.txt', 'r')

n=int(input())
hall=[]
teacher=[]
answer=False
for i in range(n):
    hall.append(list(input().split()))

for i in range(n):
    for j in range(n):
        if hall[i][j]== 'T':
            teacher.append((i,j))

dy=[0,0,1,-1]
dx=[1,-1,0,0]

def inRange(y,x):
    return y>=0 and x>=0 and y<n and x<n

def canSee():
    for y,x in teacher:
        for i in range(4):
            ny,nx = y,x
            while True:
                ny,nx = ny+dy[i], nx+dx[i]
                if not inRange(ny,nx): break
                if hall[ny][nx]== 'S':
                    return True
                elif hall[ny][nx]== 'O':
                    break
    return False

def setWall(depth):
    global answer
    if answer: return
    if depth==3:
        if not canSee():
            print("YES")
            answer=True
        return
    for i in range(n):
        for j in range(n):
            if hall[i][j]== 'X':
                hall[i][j]= 'O'
                setWall(depth+1)
                hall[i][j]= 'X'

setWall(0)

if not answer:
    print("NO")