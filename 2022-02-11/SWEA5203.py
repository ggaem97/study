import sys
sys.stdin = open('5203.txt', 'r')


def isRun(arr):
    n = len(arr)
    for i in range(0, n-2):
        # 반례) 4 5 5 6
        # if arr[i] == (arr[i+1] - 1) and arr[i] == (arr[i+2] - 2):
        if (arr[i]+1) in arr and (arr[i]+2) in arr:
            return True
    return False


def isTriplet(arr1):
    n = len(arr1)
    for i in range(n):
        count = arr1.count(arr1[i])
        if count >= 3:
            return True
    return False


T = int(input())
for tc in range(1, T+1):
    answer = 0
    cards = list(map(int, input().split()))
    player1, player2 = [], []
    for i in range(0, 12, 2):
        player1.append(cards[i])
        player2.append(cards[i+1])
    # print(player1)
    # print(player2)
    # 한명이라도 먼저 run이나 triplet되는 경우 그 분이 승리
    for i in range(4):
        result1 = isRun(player1[:i+3]) or isTriplet(player1[:i+3])
        if result1:
            answer = 1
            break
        result2 = isRun(player2[:i+3]) or isTriplet(player2[:i+3])
        if result2:
            answer = 2
            break
    print(f"#{tc} {answer}")