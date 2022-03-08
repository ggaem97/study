import sys
sys.stdin = open('a.txt', 'r')


def solution():
    n, k = map(int, input().split())
    maps = [(list(map(int, input().split()))) for _ in range(n)]
    s, x, y = map(int, input().split())

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    x -= 1
    y -= 1
    if maps[x][y] != 0:
        print(maps[x][y])
        return

    q = []
    visited = [(x, y)]
    maps[x][y] = 1001
    for i in range(s):
        temp = []
        while visited:
            print('visited', visited)
            x, y = visited.pop()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if nx > -1 and ny > -1 and nx < n and ny < n:
                    if maps[nx][ny] != 0 and maps[nx][ny] != 1001:
                        q.append(maps[nx][ny])
                        print('q', q)
                    elif maps[nx][ny] == 0:
                        temp.append((nx, ny))
                        print('tmp', temp)
                    maps[nx][ny] = 1001
        visited = temp[:]
        print('after loop visited', visited)
        if q:
            print(min(q))
            return
    if not q:
        print(0)


solution()
