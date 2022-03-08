import sys
sys.stdin = open('14891.txt', 'r')
chain = [list(input()) for _ in range(4)]
k = int(input())
# 왼쪽으로 회전
def turnLeft(s):
    # data = s[1:] + s[0]
    # return data
    data = s.pop(0)
    s.append(data)
    return s
# 오른쪽을 회전
def turnRight(s):
    # data = s[-1] + s[:-1]
    # return data
    data = s.pop()
    s.insert(0, data)
    return s
def move(i, d):
    # 시계 방향
    if d == 1:
        chain[i] = turnRight(chain[i])
    # 반시계 방향
    elif d == -1:
        chain[i] = turnLeft(chain[i])

for _ in range(k):
    idx, direction = map(int, input().split())
    idx -= 1
    check = [0]*4
    check[idx] = direction
    # 왼쪽 톱니바퀴 확인
    # for i in range(1, 4):
    for i in range(idx, 0, -1):
        if chain[i][6] != chain[i-1][2]:
            check[i-1] = (-1)*check[i]
    # 오른쪽 톱니바퀴 확인
    for i in range(idx, 3):
        if chain[i][2] != chain[i+1][6]:
            check[i + 1] = (-1)*check[i]
    for i in range(4):
        move(i, check[i])

res = 0
for i in range(4):
    if chain[i][0] == '1':
        res += 2**i
print(res)