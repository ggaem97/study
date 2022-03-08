import sys
sys.stdin = open('gear.txt', 'r')

gears = [list(map(int, map(str, input()))) for _ in range(4)]
print(gears)
K = int(input())
turn = [tuple(map(int, input().split())) for _ in range(K)]
print(turn)


# 반시계 방향으로 이동 : 왼쪽으로 한칸씩 이동
def turnLeft(gear):
    tooth = gear.pop(0)
    gear.append(tooth)


# 시계 방향으로 이동 : 오른쪽으로 이동
def turnRight(gear):
    tooth = gear.pop()
    gear.insert(0, tooth)


for number, direction in turn:
    number -= 1
    # 어떻게 회전을 퍼지게 하지 ?
    

turnRight([0,0,1,0,0,0,0,1])