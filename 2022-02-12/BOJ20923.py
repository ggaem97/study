import sys
sys.stdin = open('20923.txt', 'r')
# 카드 개수, 게임 횟수
n, m = map(int, input().split())
do_card = []
su_card = []
for _ in range(n):
    a, b = map(int, input().split())
    do_card.append(a)
    su_card.append(b)
print('do', do_card)
print('su', su_card)
print('game start!')
groundD = []
groundS = []
# 진사람의 카드를 가져오는 함수
def getCard(result):
    global do_card, su_card, groundD, groundS
    groundS.reverse()
    groundD.reverse()
    # 도도가 이겼다면
    if result == 1:
        print('do getCard')
        do_card = groundD + groundS + do_card
    # 수연이가 이겼다면
    else:
        print('su getCard')
        su_card = groundS + groundD + su_card
    groundS, groundD = [], []


for _ in range(m):
    # 둘중에 하나라도 카드가 소진되면 게임 종료
    if not do_card or not su_card:
        break
    print('d card:', do_card[-1], 's card:', su_card[-1])
    # 도도의 순서
    d = do_card.pop()
    # 그라운드가 하나라도 차있는 경우
    if groundD or groundS:
        ground = groundS + groundD
        # 숫자 5가 있는지 검사
        if 5 in ground:
            getCard(1)
    groundD.append(d)
    if d == 5:
        getCard(1)

    # 수연의 순서
    s = su_card.pop()
    # 그라운드가 모두 채워져 있는 경우
    if groundD and groundS:
        # 합이 5가 되는지 검사
        total = groundD[-1] + groundS[-1]
        if total == 5:
            getCard(0)
    # 수연이 그라운드만 비어있는 경우
    elif groundD and not groundS:
        groundS.append(s)
        # 합이 5가 되는지 검사
        total = groundD[-1] + groundS[-1]
        if total == 5:
            getCard(0)
        continue
    groundS.append(s)

dLen, sLen = len(do_card), len(su_card)
if dLen > sLen:
    print('do')
elif dLen < sLen:
    print('su')
else:
    print('dosu')