import sys
sys.stdin = open('1107.txt', 'r')


def getDirection(i, s, e):
    while i + s >= 0 or i + e < n:
        if i+s in button:
            return 1
        elif i+e in button:
            return -1
        else:
            i -= 1
            e += 1


# 첫번째 자리가 같거나 큰 경우 -> + 방향으로 탐색
# 첫번째 자리가 작은 경우 -> - 방향으로 탐색
def pushButton():
    result = []
    direction = 1
    for idx, c in enumerate(channel):
        if c in button:
            result.append(c)
            direction = getDirection(idx, -1, 1)
            continue
        if direction == 1:
            pass

    print(result)
    return result


# 현재 보고 있는 채널 번호 100
channel = list(map(int, input())) # 이동하고자 하는 채널
# print('channel', channel)
n = int(input())
unable = [] # 누를 수 없는 버튼
if channel == 100:
    print(0)
elif n == 0:
    print(len(channel))
else:
    unable = list(map(int, input().split()))
    button = [i for i in range(10) if i not in unable]
    print(button)
    r = pushButton()
    answer = len(r) + abs(int(''.join(map(str, r))) - int(''.join(map(str, channel))))
    print(answer)
