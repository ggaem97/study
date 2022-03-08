import sys
sys.stdin = open('14891.txt', 'r')
chain = [''] + [input() for _ in range(4)]
k = int(input())
print(chain)


def turnLeft(s):
    data = s[1:] + s[0]
    return data

def turnRight(s):
    data = s[-1] + s[:-1]
    return data


for _ in range(k):
    idx, direction = map(int, input().split())
    # 옆으로 퍼지게 하는 것은 어떻게 구현하지? 연쇄작용
    if idx == 1:
        # 시계방향
        if direction == 1:
            pass
        # 반시계방향
        elif direction == -1:
            pass
    elif idx == 4:
        # 시계방향
        if direction == 1:
            chain[idx] = turnRight(chain[idx])
        if chain[idx - 1][2] != chain[idx][6]:
            chain[idx-1] = turnLeft(chain[idx-1])
        # 반시계방향
        elif direction == -1:
            chain[idx] = turnLeft(chain[idx])
    else:
        # 시계방향
        if direction == 1:
            pass
        # 반시계방향
        elif direction == -1:
            pass