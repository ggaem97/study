import sys
sys.stdin = open('2583.txt', 'r')
m, n, k = map(int, input().split())
board = [[0]*n for _ in range(m)]
position = [(1,0), (0,1), (-1,0), (0,-1)]


def dfs(x, y, count):
    board[x][y] = 1
    for dx, dy in position:
        nx = dx + x
        ny = dy + y
        if 0<=nx<m and 0<=ny<n:
            if board[nx][ny] == 0:
                count = dfs(nx, ny, count+1)
    return count


for _ in range(k):
    a, b, c, d = map(int, input().split())
    for x in range(b, d):
        for y in range(a, c):
            board[m-1-x][y] = 1
area = []
for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            area.append(dfs(i,j,1))

print(len(area))
print(*sorted(area))