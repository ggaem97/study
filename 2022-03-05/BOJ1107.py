import sys
sys.stdin = open('1107.txt', 'r')
# 현재 보고 있는 채널 번호 100
channel = list(map(int, input()))
print('channel', channel)
n = int(input())
unable = []
if n != 0:
    unable = list(map(int, input().split()))
button = []
for i in range(10):
    if i in unable:
        continue
    button.append(i)
print(button)
print(unable)
result = []


def pushButton():
    for c in channel:
        s, e = -1, +1
        if c in button:
            result.append(c)
            continue
        while s <= e:
            if c+s in button:
                result.append(c+s)
                break
            elif c+e in button:
                result.append(c+e)
                break
            else:
                s -= 1
                e += -1


print(result)
if int(''.join(map(str, channel))) == 100:
    print(0)
else:
    pushButton()
    answer = len(result) + abs(int(''.join(map(str, result))) - int(''.join(map(str, channel))))
    print(answer)
