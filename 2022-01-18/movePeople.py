import sys
sys.stdin = open('in3.txt', 'r')

n, a, b = map(int, input().split())
board = [list(map(input().split())) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

for i in range(n):
    for j in range(n):
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            if 0<=x<n and 0<=y<n:
                distance = abs(board[i][j] - board[x][y])
                if a <= distance <= b:
                    pass