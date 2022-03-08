import sys
sys.setrecursionlimit(10**4)
sys.stdin = open('2583.txt', 'r')

m, n, k = map(int, input().split())
board = [[0]*n for _ in range(m)]

dX = [1,0,-1,0]
dY = [0,1,0,-1]


def dfs(y, x, arr, count):
    arr[y][x] = 1
    for dx, dy in zip(dX, dY):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if arr[ny][nx] == 0:
                count = dfs(ny, nx, arr, count+1)
    return count


# 직사각형 세팅하기
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            board[y][x] = 1

area = []
for i in range(m):
    for j in range(n):
        # '0'이라면 영역 구하기
        if board[i][j] == 0:
            area += [dfs(i, j, board, 1)]
print(len(area))
print(*sorted(area))