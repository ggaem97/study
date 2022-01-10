import datetime
# print(datetime.datetime.now())
# 2021-12-19 14:15:02.107338
import sys
sys.stdin = open('in4.txt','r')
n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
union = []
sum = 0
for i in range(n):
    print(board[i])
print()
#인구이동
dx = [1,0,-1,0]
dy = [0,1,0,-1]


def makeUnion(x,y):
    global sum
    global union

    for k in range(4):
        xx = dx[k] + x
        yy = dy[k] + y
        if 0<=xx<n and 0<=yy<n:
            gap = abs(board[xx][yy]-board[x][y])
            if l <= gap <= r and (xx, yy) not in union:
                union.append((xx, yy))
                sum += board[xx][yy]
                makeUnion(xx,yy)
                print(union)

def setNumOfPeople():
    global sum
    global union
    result = sum//len(union)
    for x,y in union:
        board[x][y] = result
    union = []
    sum = 0

for i in range(n):
    for j in range(n):
        pass
        # 원소 하나 찾아서 리스트 구하고 리스트에 인구수 할당
# 갭 차이 나는 원소 하나도 없으면 0을 출력
# 조건을 만족하는 갭 차이 나는 원소 존재할 경우 리스트 생성
# 리스트에 해당하는 인덱스에 인구수 할당
# 반복.... 갭차이 나는 원소가 하나도 없을 때까지
makeUnion(0,0)
# setNumOfPeople()
print(board)


