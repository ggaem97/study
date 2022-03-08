import sys
sys.stdin = open('shark.txt', 'r')
n,m = map(int, input().split())
aquarium = [list(map(int, input().split())) for _ in range(n)]
dx = [1,0,-1,0,-1,1,1,-1]
dy = [0,1,0,-1,-1,1,-1,1]


def spread(x, y):
    for k in range(8):
        nx = dx[k] + x
        ny = dy[k] + y
        if 0<= nx < n and 0<= ny < m:
            if aquarium[nx][ny] == 0:
                aquarium[nx][ny] = aquarium[x][y] + 1


def checkZero(lst):
    for i in range(n):
        for j in range(m):
            if lst[i][j] == 0:
                return True
    return False


k = 1
while True:
    if not checkZero(aquarium):
        break
    for i in range(n):
        for j in range(m):
            if aquarium[i][j] == k:
                spread(i, j)
    k += 1

res = 0
for i in range(n):
    rowMax = max(aquarium[i])
    res = max(rowMax, res)
print(res-1)

