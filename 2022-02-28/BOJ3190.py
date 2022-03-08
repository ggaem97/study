from collections import deque
import sys
sys.stdin = open('3190.txt', 'r')
n = int(input())
board = [[0]*n for _ in range(n)]
k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1
p = {}
for _ in range(int(input())):
    a, b = input().split()
    p[int(a)] = b

# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def turn(now, D):
    result = 0
    if D == 'D':
        if now == 3:
            return 0
        return now + 1
    else:
        if now == 0:
            return 3
        return now - 1


t = 0
# bfs로 풀이
def dummy():
    global t
    x, y = 0, 0
    direction = 0
    # 첫 위치에 뱀 초기화
    board[x][y] = 2
    # 뱀의 위치 정보 저장
    snake = deque([(x, y)])
    while True:
        t += 1
        x, y = dx[direction] + x, dy[direction] + y
        # 벽에 닿으면 종료
        if x < 0 or x >= n or y < 0 or y >= n:
            break
        # 자기 몸에 닿으면 종료
        if board[x][y] == 2:
            break
        # 사과가 없다면 꼬리 제거
        if board[x][y] != 1:
            sx, sy = snake.popleft()
            board[sx][sy] = 0
        board[x][y] = 2
        snake.append((x, y))
        if t in p.keys():
            time, d = t, p[t]
            direction = turn(direction, d)
            del p[time]

dummy()
print(t)



