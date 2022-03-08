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

print('do_card, su_card', do_card, su_card)
groundD.append(do_card.pop())
for i in range(1, m):
    # 둘중에 하나라도 카드가 소진되면 게임 종료
    if not do_card or not su_card:
        break
    # 수연이 순서
    if i%2 != 0:
        # 그라운드가 모두 빈 상태
        if not groundD and not groundS:
            groundS.append(su_card.pop())


    # 도도 차례
    else:
        pass


dLen, sLen = len(do_card), len(su_card)
if dLen > sLen:
    print('do')
elif dLen < sLen:
    print('su')
else:
    print('dosu')