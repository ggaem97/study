import copy
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
def fish_move(d_arr, s_arr, x, y):
    # 1~16까지 물고기 move
    for k in range(1, 17):
        # 잡아 먹힌 물고기는 무시
        if not find_fish(s_arr, k):
            continue
        xx, yy = find_fish(s_arr, k)

        D = d_arr[xx][yy]
        # 이동이 가능한 경우 물고기 위치 방향 정보 swap
        for _ in range(8):
            fx, fy = xx + dx[D-1], yy + dy[D-1]
            # 벽이거나 상어가 있는 경우 회전
            if fx < 0 or fx >= 4 or fy < 0 or fy >= 4 or (fx == x and fy == y):
                D = turn45(D)
            else:
                # 방향 정보 갱신
                d_arr[xx][yy] = D
                # 물고기 교환
                s_arr[xx][yy], s_arr[fx][fy] = s_arr[fx][fy], s_arr[xx][yy]
                d_arr[xx][yy], d_arr[fx][fy] = d_arr[fx][fy], d_arr[xx][yy]
                break


# 상어가 이동 가능한 좌표 구하기
def possible_move(d_arr, s_arr, x, y):
    global result

    # print('x, y', x, y,'에 있는 상어가 움직입니다..')
    positions = []
    # 상어의 좌표, 상어의 방향
    sx, sy = x, y
    sd = d_arr[x][y]
    # 상어가 위치할 수 있는 좌표 정보 확인
    for _ in range(4):
        sx += dx[sd-1]
        sy += dy[sd-1]
        if 0 <= sx < 4 and 0 <= sy < 4:
            if s_arr[sx][sy] != 0:
                positions.append([sx, sy])
    # 이동가능한 경로가 없는 경우
    if not positions:
        return False
    return positions


# 물고기 위치 찾기
def find_fish(arr, K):
    for i in range(4):
        for j in range(4):
            if arr[i][j] == K:
                return [i, j]
    # 상어가 식사해버려서 번호를 못찾는 경우
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


def dfs(d_arr, s_arr, x, y, total):
    global result, space
    s_arr = copy.deepcopy(s_arr)  # 리스트를 통째로 복사
    d_arr = copy.deepcopy(d_arr)
    total += s_arr[x][y] # 물고기 식사
    s_arr[x][y] = 0 # 잡아먹힌 물고기 제거
    # 물고기 이동
    fish_move(d_arr, s_arr, x, y)

    # 상어 move
    p = possible_move(d_arr, s_arr, x, y)
    if not p:
        result = max(total, result)
        return
    for next_x, next_y in p:
        dfs(d_arr, s_arr, next_x, next_y, total)


dfs(direction, space, 0, 0, 0)
print(result)