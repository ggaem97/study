import sys

sys.stdin = open('1.txt', 'r')

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


def get_count(tmp):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                cnt += 1
    return cnt


def solution(count):
    global mxCnt
    tmp = [[0]*m for _ in range(n)]

    if count == 3:
        # 바이러스를 전파시킬 임시 2차원 연구소 생성
        for i in range(n):
            for j in range(m):
                tmp[i][j] = board[i][j]

        # 바이러스 감염
        for i in range(n):
            for j in range(m):
                if tmp[i][j] == 2:
                    virus(tmp, i, j)

        result = max(result, get_count(tmp))

    else:
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0:
                    board[i][j] = 1
                    count += 1
                    solution(count)
                    count -= 1
                    board[i][j] = 0

    return result

mxCnt = 0
print(solution(0))