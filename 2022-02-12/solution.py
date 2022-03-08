import sys
sys.stdin = open('2583.txt', 'r')


def dfs(x, y):
    stack = [(x, y)]
    board[x][y] = True
    num = 1

    while stack:
        x, y = stack.pop()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            if not board[nx][ny]:
                stack.append((nx, ny))
                board[nx][ny] = True
                num += 1
    ## 마지막에 영역의 크기를 리스트에 저장한다.
    empty_list.append(num)


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    board = [[False] * m for _ in range(n)]

    ## 직사각형이 존재하는 영역은 True로 변환
    for _ in range(k):
        y1, x1, y2, x2 = map(int, input().split())
        for i in range(x1, x2):
            for j in range(y1, y2):
                board[i][j] = True
    ## 동 남 서 북
    dxs = (0, 1, 0, -1)
    dys = (1, 0, -1, 0)

    empty_list = []
    for i in range(n):
        for j in range(m):
            if not board[i][j]:  # False 라면
                dfs(i, j)  # 영역의 크기를 empty_list에 추가시키는 함수

    print(len(empty_list))
    print(' '.join(map(str, sorted(empty_list))))