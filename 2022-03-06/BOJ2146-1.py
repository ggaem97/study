from collections import deque
import sys
sys.stdin = open('2146.txt', 'r')
n = int(input())
bridge = [list(map(int, input().split())) for _ in range(n)]
last_x, last_y = 0, 0
for i in range(n):
    for j in range(n):
        if bridge[i][j] == 1:
            last_x, last_y = i, j
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


# 여기에서 문제 발생 : 최단거리 보장 못함
def getMinDistance(my_area, color):
    global cnt
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
    for x, y in my_area:
        que = deque([(x, y, 0)])
        while que:
            x, y, c = que.popleft()
            for dx, dy in move:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    if bridge[nx][ny] == 1:
                        return c
                    que.append((nx, ny, c+1))
    # return cnt

cnt = 1e9
c = 26

for i in range(n):
    for j in range(n):
        area = []
        if bridge[i][j] == 1:
            # 본인 섬 색칠 (다른 섬이랑 구분할 수 있도록)
            c += 1
            area = myArea(i, j, c)
            # 마지막 섬에 도달한 경우
            if (last_x, last_y) in area:
                break
            getMinDistance(area, c)
print(cnt)