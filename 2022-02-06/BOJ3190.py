import sys
sys.stdin = open('3190.txt', 'r')
# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(d, check):
    print('turned!')
    # 왼쪽으로 회전
    if d == 'L':
        if check == 0:
            return 3
        return check - 1
    # 오른쪽으로 회전
    else:
        if check == 3:
            return 0
        return check + 1


n = int(input())
k = int(input())
board = [[0]*n for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1
l = int(input())
table = []
for _ in range(l):
    x, c = input().split()
    x = int(x)
    table.append((c, x))
for bb in board:
    print(bb)
print(table)
print('game start! ')
print()
t = 0
xx, yy = 0, 0
position = 0
while True:
    for x, c in table:
        if t == x:
            turn(position, c)
    xx += dx[position]
    yy += dy[position]
    if 0 <= xx < n and 0 <= yy < n:
        print(xx, yy)
        if board[xx][yy] == 1:
            print('wow')
            break
    t += 1
    for i in range(n):
        print(board[i])
    print()
    if t == table[-1][1]:
        break