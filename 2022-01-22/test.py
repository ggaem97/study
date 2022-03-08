import sys
sys.stdin = open('gear.txt', 'r')
gears = [list(map(int, map(str, input()))) for _ in range(4)]
K = int(input())
turn = [tuple(map(int, input().split())) for _ in range(K)]


# 반시계 방향으로 이동 : 왼쪽으로 한칸씩 이동
def turnLeft(gear):
    tooth = gear.pop(0)
    gear.append(tooth)


# 시계 방향으로 이동 : 오른쪽으로 이동
def turnRight(gear):
    tooth = gear.pop()
    gear.insert(0, tooth)


for num, direction in turn:
    num -= 1
    # 어떻게 회전을 퍼지게 하지 ?
    directions = [0]*4
    directions[num] = direction
    # 오른쪽 톱니바퀴 검사
    for i in range(num, 3):
        if gears[i][2] != gears[i+1][6]:
            # directions[i+1] = direction*(-1)
            directions[i+1] = directions[i]*(-1)
    # 왼쪽 톱니바퀴 검사
    for i in range(num, 0, -1):
        if gears[i][6] != gears[i-1][2]:
            directions[i-1] = directions[i]*(-1)
    # print(directions)
    # 정보에 대해 회전 진행
    for i in range(4):
        if directions[i] == -1:
            turnLeft(gears[i])
        elif directions[i] == 1:
            turnRight(gears[i])
res = 0
for i in range(4):
    if gears[i][0] == 1:
        res += pow(2,i)
print(res)