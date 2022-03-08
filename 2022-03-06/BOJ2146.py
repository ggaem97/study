from collections import deque
import sys
sys.stdin = open('2146.txt', 'r')
n = int(input())
bridge = [list(map(int, input().split())) for _ in range(n)]
for bb in bridge:
    print(bb)
print()
move = [(1,0),(0,1),(0,-1),(-1,0)]


def myArea(x, y, color):
    que = deque([(x, y)])
    bridge[x][y] = color
    my_area = [(x,y)]
    while que:
        x, y = que.popleft()
        for dx, dy in move:
            nx = dx + x
            ny = dy + y
            if 0 <= nx < n and 0 <= ny < n:
                if bridge[nx][ny] == 1:
                    bridge[nx][ny] = color
                    que.append((nx, ny))
                    my_area.append((nx, ny))
    return my_area


def getMinDistance(my_area, color):
    cnt = 1e9
    # for x, y in my_area:
    #     i, j = x, y
    #     for dx, dy in move:
    #         while True:
    #             x += dx + x
    #             y += dy + y
    #             if x >= n or x < 0 or y >= n or y < 0:
    #                 break
    #             if bridge[x][y] != 0 and bridge != color:
    #                 distance = abs(i-x)**2 + abs(j-y)**2
    #                 cnt = min(cnt, distance)
    que = deque([])
    for a in my_area:
        x, y = a
        que.append((x, y, 0))
    # print(que)
    while que:
        x, y, c = que.popleft()
        # print(x, y, c)
        if x < 0 or x >= n-1 or y < 0 or y >= n-1:
            continue
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            # print('nx, ny', nx, ny)
            if bridge[nx][ny] == 0:
                que.append((nx, ny, c+1))
            elif bridge[nx][ny] != 0 and bridge[nx][ny] != color:
                cnt = min(c, cnt)
                return cnt
    return cnt


result = 1e9
c = 26
for i in range(n):
    for j in range(n):
        area = []
        if bridge[i][j] == 1:
            # 본인 섬 색칠 (다른 섬이랑 구분할 수 있도록)
            area = myArea(i, j, c)
            c += 1
        result = min(result, getMinDistance(area, c))
        # 0으로 색칠
        print('result', result)
        for x, y in area:
            bridge[x][y] = 0

    for bb in bridge:
        print(bb)
    print()
print(result)