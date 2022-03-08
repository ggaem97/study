from itertools import combinations

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]


#바이러스 전파
def virus(tmp, x, y):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    for k in range(4):
        xx = x+dx[k]
        yy = y+dy[k]
        if 0<=xx<n and 0<=yy<m and tmp[xx][yy] == 0:
            tmp[xx][yy] = 2
            virus(tmp, xx, yy)


def count(tmp):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                cnt += 1
    return cnt


def solution():
    result = 0
    tmp = [[0]*m for _ in range(n)]

    # 빈칸 좌표 구하기
    zeroIdxs = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                zeroIdxs.append((i, j))

    for coordinates in list(combinations(zeroIdxs, 3)):
        # 3개의 빈벽에 벽 설치
        for coordinate in coordinates:
            x, y = coordinate
            board[x][y] = 1

        # 바이러스를 전파시킬 임시 2차원 연구소 생성
        for i in range(n):
            for j in range(m):
                tmp[i][j] = board[i][j]

        # 바이러스 감염
        for i in range(n):
            for j in range(m):
                if tmp[i][j] == 2:
                    virus(tmp, i, j)

        result = max(result, count(tmp))

        # 설치한 벽 제거
        for coordinate in coordinates:
            x, y = coordinate
            board[x][y] = 0
    return result


print(solution())