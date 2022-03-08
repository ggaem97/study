lst = [(3, 'D'), (20, 'D'), (15, 'U')]
#            북 동 남 서
positions = [0, 1, 2, 3]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
t = 0
direction = 1
board = [[0]*4 for _ in range(4)]

def switchPosition(s):
    global direction
    # 오른쪽으로 90도 회전
    if s == 'D':
        p += 1
        if p == 4:
            p = 0
    else:
        p -= 1
        if p == -1:
            p = 3
    return p


x = 0
y = 0
print(x,y)
# lst = [(3, 'D'), (20, 'D'), (15, 'U')]
while True:
    t += 1
    if t == lst[0][0]:
        if 0<=x<4 and 0<=y<4:
            data = lst.pop(0)
            direction = switchPosition(data[1])

    x = x+dx[direction]
    y = y+dy[direction]
    # print(dx[p],dy[p])
    if x >= 4 or x < 0 or y >= 4 or y < 0:
        break
    print('p:', direction, end=' ')
    print('t:', x, y)
