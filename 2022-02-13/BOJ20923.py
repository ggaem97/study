from collections import deque
import sys
sys.stdin = open('20923.txt', 'r')
n, m = map(int, input().split())
dDeck, sDeck = deque(), deque()
dGround, sGround = deque(), deque()


def appendStack(result):
    global dGround, sGround, dDeck, sDeck
    # 도도가 이긴 경우
    if result == 2:
        while sGround:
            dDeck.append(sGround.pop())
        while dGround:
            dDeck.append(dGround.pop())
    else:
        while dGround:
            sDeck.append(dGround.pop())
        while sGround:
            sDeck.append(sGround.pop())


for _ in range(n):
    a, b = map(int, input().split())
    dDeck.appendleft(a)
    sDeck.appendleft(b)

# 도도와 수연이가 카드를 내는 총합이 'm'
while True:
    # 도도의 차례
    dCard = dDeck.popleft()
    dGround.appendleft(dCard)

    # 도도의 덱이 비어있는 경우 종료
    if not dDeck:
        break

    # 도도가 이길 경우
    if dCard == 5:
        # 더미 합치기
        appendStack(2)

    # 수연이가 이길 경우
    if sGround and dGround and (sGround[0] + dGround[0]) == 5:
        appendStack(1)

    m -= 1
    if m == 0:
        break

    # 수연의 차례
    sCard = sDeck.popleft()
    sGround.appendleft(sCard)

    # 수연의 덱이 비어있는 경우 종료
    if not sDeck:
        break

    # 도도가 이길 경우
    if sCard == 5:
        appendStack(2)

    # 수연이가 이길 경우
    if sGround and dGround and (sGround[0] + dGround[0]) == 5:
        appendStack(1)

    m -= 1
    if m == 0:
        break

s, d = len(sDeck), len(dDeck)
if s == d:
    print('dosu')
elif s < d:
    print('do')
else:
    print('su')