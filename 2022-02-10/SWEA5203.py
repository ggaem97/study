import sys
sys.stdin = open('5203.txt', 'r')
T = int(input())

def isRun(arr1):
    # tmp = sorted(arr1)
    # n = len(arr1)
    # for i in range(0, n-2):
    #     if tmp[i] == (tmp[i+1] - 1) and tmp[i] == (tmp[i+2] - 2):
    #         return True
    return False


def isTriplet(arr):
    # tmp = sorted(arr)
    # n = len(arr)
    # for i in range(n):
    #     count = tmp.count(tmp[i])
    #     if count >= 3:
    #         return True
    return False


print(T)
for tc in range(1, T+1):
    answer = 0
    cards = list(map(int, input().split()))
    player1 = []
    player2 = []
    for i in range(0, 12, 2):
        player1.append(cards[i])
        player2.append(cards[i+1])
     # 한명이라도 먼저 run이나 triplet되는 경우 그 분이 승리
    for i in range(4):
        result1 = isRun(player1[:i+3]) or isTriplet(player1[:i+3])
        result2 = isRun(player2[:i+3]) or isTriplet(player2[:i+3])
        if result1 and not result2:
            answer = 1
            break
        elif result2 and not result1:
            answer = 2
            break
        else:
            continue
    print(f"#{tc} {answer}")