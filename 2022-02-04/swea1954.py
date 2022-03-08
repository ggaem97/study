import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
# 동 남 서 북
dx = [0,1,0,-1]
dy = [1,0,-1,0]


def turn(position):
    if position == 3:
        return 0
    return position+1


for t in range(1, T+1):
    N = int(input())
    snail = [[0]*N for _ in range(N)]
    x, y = 0, 0
    snail[x][y] = 1
    p = 0
    for n in range(2, N**2+1):
        nx = x + dx[p]
        ny = y + dy[p]
        if nx<0 or nx>=N or ny<0 or ny>=N or snail[nx][ny] != 0:
            p = turn(p)
            nx = x + dx[p]
            ny = y + dy[p]
        snail[nx][ny] = n

        x = nx
        y = ny
    print(f'#{t}')
    for i in range(N):
        for j in range(N):
            print(snail[i][j], end=' ')
        print()