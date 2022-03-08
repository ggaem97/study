import sys
sys.stdin = open('marble.txt', 'r')
n, m = map(int, input().split())
frame = [input() for _ in range(n)]
print(frame)


def DFS(x, y):
    d = [(1,0), (0,1), (-1,0), (0,-1)]
    cnt = 0
    for dx, dy in d:
        cnt = 0
        if 0<=x+dx<n and 0<=y+dy<n:
            print(x+dx, dy+y)
            if cnt > 10:
                break
            if frame[x+dx][y+dy] == 'O':
                cnt += 1
                break
            while frame[x+dx][y+dy] != '#':
                x += dx
                y += dy
                cnt += 1

    print(cnt)


for i in range(n):
    for j in range(m):
        if frame[i][j] == 'R':
            DFS(i, j)