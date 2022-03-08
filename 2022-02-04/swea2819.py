import sys
sys.stdin = open('input.txt', 'r')


def dfs(idx, row, col, num):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    num += board[row][col]
    if idx == 6:
        answer.append(num)
        return
    for i in range(4):
        if 0<=row+dx[i]<4 and 0<=col+dy[i]<4:
            dfs(idx+1, row+dx[i], col+dy[i], num)


T = int(input())
for t in range(T):
    board = [list(map(str, input().split())) for _ in range(4)]
    answer = []
    for x in range(4):
        for y in range(4):
            dfs(0, x, y, '')

    answer = set(answer)
    print(f'#{t+1} {len(answer)}')