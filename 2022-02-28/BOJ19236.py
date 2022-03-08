import sys
sys.stdin = open('19236.txt', 'r')

# 1 2 3 4 5 6 7 8
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]


# 반시계로 회전
def turn45(D):
    if D == 8:
        return 1
    return D+1


# 물고기 이동
def fish_move(xx, yy):
    D = direction[xx][yy]
    # 이동 가능한 경우와 이동이 불가능한 경우 나눔
    # 이동이 가능한 경우 물고기 위치 방향 정보 swap
    # 이동이 불가능한 경우 stay
    for _ in range(8):
        fx, fy = xx + dx[D-1], yy + dy[D-1]
        # 벽이거나 상어가 있는 경우 회전
        if fx < 0 or fx >= 4 or fy < 0 or fy >= 4 or (fx == x and fy == y):
            D = turn45(D)
        else:
            # 방향 정보 갱신
            direction[xx][yy] = D
            # 물고기 교환
            space[xx][yy], space[fx][fy] = space[fx][fy], space[xx][yy]
            direction[xx][yy], direction[fx][fy] = direction[fx][fy], direction[xx][yy]
            break


def shark_move():
    global result, d, x, y
    tmp_x, tmp_y = 0, 0
    val = 0
    # 상어의 좌표, 상어의 방향
    sx, sy = x, y
    sd = direction[x][y]
    # 상어가 위치할 수 있는 좌표 정보 확인
    for _ in range(4):
        sx += dx[sd-1]
        sy += dy[sd-1]
        if 0 <= sx < 4 and 0 <= sy < 4:
            if val < space[sx][sy]:
                val = space[sx][sy]
                tmp_x, tmp_y = sx, sy
    print(space[tmp_x][tmp_y])
    # 제일 값이 큰놈 골라 result에 저장
    result += space[tmp_x][tmp_y]
    # 상어의 방향, 좌표 정보 갱신
    d = direction[tmp_x][tmp_y]
    x, y = tmp_x, tmp_y
    # 가장 큰 값이 들어있는 곳에 물고기 제거
    space[tmp_x][tmp_y] = 0


def find_fish(K):
    for i in range(4):
        for j in range(4):
            if space[i][j] == K:
                return [i, j]
    return False

result = 0
space = [[0]*4 for _ in range(4)]
direction = [[0]*4 for _ in range(4)]
for i in range(4):
    x1, d1, x2, d2, x3, d3, x4, d4 = map(int, input().split())
    space[i][0], direction[i][0] = x1, d1
    space[i][1], direction[i][1] = x2, d2
    space[i][2], direction[i][2] = x3, d3
    space[i][3], direction[i][3] = x4, d4
for ss in space:
    print(ss)
print()
for dd in direction:
    print(dd)
x, y = 0, 0
d = direction[x][y]
result += space[x][y]
# 잡아 먹힌 물고기 삭제
space[x][y] = 0
for k in range(1, 17):
    # 1~16까지 물고기 move
    if not find_fish(k):
        continue
    find_x, find_y = find_fish(k)
    fish_move(find_x, find_y)

# 상어 move
shark_move()
for ss in space:
    print(ss)
print()
for dd in direction:
    print(dd)
print()
print(result)