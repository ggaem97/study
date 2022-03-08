import sys
# sys.stdin = open('snake2', 'r')
n = int(sys.stdin.readline().strip())
data = [[0] * (n + 1) for i in range(n + 1)]
k = int(sys.stdin.readline().strip())
# data[0][0] = 2
# 보고 있는 방향 : 동쪽
# direction = 1
info = []

# 사과가 있는 경우 1로 처리
for i in range(k):
    x, y = map(int, sys.stdin.readline().strip().split())
    data[x - 1][y - 1] = 1

#     동  남  서  북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def switchPosition(s, direction):
    # 오른쪽으로 90도 회전
    if s == 'D':
        direction = (direction + 1) % 4
        # direction += 1
        # if direction == 4:
        #     direction = 0
    else:
        direction = (direction - 1) % 4
        # p -= 1
        # if p == -1:
        #     p = 3
    return direction

m = int(sys.stdin.readline().strip())
for i in range(m):
    time, position = map(str, sys.stdin.readline().strip().split())
    t = int(time)
    info.append((t, position))

info.sort(key=lambda x: int(x[0]))
# print(info)
# 게임 시작
def game():
    x, y = 0, 0
    t = 0
    data[x][y] = 2
    direction = 0
    q = [(x,y)]
    # for i in range(n):
    #     for j in range(n):
    #         print(data[i][j], end=' ')
    #     print()
    # print()
    # print("let's start!!")
    while True:
        xx = x+dx[direction]
        yy = y+dy[direction]

        if 0<=xx<n and 0<=yy<n and data[xx][yy] != 2:
            # data[xx][yy] = 2
            # 사과가 없다면
            if data[xx][yy] == 0:
                data[xx][yy] = 2
                q.append((xx,yy))
                px, py = q.pop(0)
                # 꼬리 삭제
                data[px][py] = 0
            # 사과가 있다면
            if data[xx][yy] == 1:
                data[xx][yy] = 2
                q.append((xx,yy))
        else:
            t += 1
            break
        x = xx
        y = yy
        t += 1
        if info and t == info[0][0]:
            direction = switchPosition(info[0][1], direction)
            info.pop(0)

        # for i in range(n):
        #     for j in range(n):
        #         print(data[i][j], end=' ')
        #     print()
        # print()

    return t

mxCnt = game()
print(mxCnt)