import sys
sys.setrecursionlimit(10**4)
# sys.stdin = open('2468', 'r')
n = int(input())
board = []
min_val, max_val = 100, 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(depth, x, y):
    tmp[x][y] = 0
    for xx, yy in zip(dx, dy):
        nx = xx + x
        ny = yy + y
        if 0 <= nx < n and 0 <= ny < n:
            if tmp[nx][ny] > depth:
                dfs(depth, nx, ny)
    return 1


for _ in range(n):
    data = list(map(int, input().split()))
    board.append(data)
    min_val = min(min_val, min(data))
    max_val = max(max_val, max(data))

tmp = [[0]*n for _ in range(n)]
answer = 1
count = 0
for target in range(min_val, max_val):
    for i in range(n):
        for j in range(n):
            tmp[i][j] = board[i][j]
    count = 0
    for i in range(n):
        for j in range(n):
            if tmp[i][j] > target:
                count += dfs(target, i, j)
    answer = max(answer, count)
print(answer)