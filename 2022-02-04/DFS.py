def dfs(x, y):
    d = [(1,0),(0,1),(-1,0),(0,-1)]
    visited[x][y] = True

    for dx, dy in d:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny]:
                board[nx][ny] = board[x][y] + 1

n = 4
board = [[1]*n for _ in range(n)]
visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)

for i in range(n):
    print(board[i])
