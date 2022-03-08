import sys
sys.stdin = open('10816.txt', 'r')
n = int(input())
cards = sorted((map(int, input().split())))
m = int(input())
targets = list(map(int, input().split()))
result = []

def findLeftIdx(target):
    start, end = 0, n-1
    while start <= end:
        mid = (start + end)//2
        if cards[mid] < target:
            start = mid + 1
        elif cards[mid] > target:
            end = mid - 1
        elif cards[mid] == target and (mid == 0 or cards[mid-1] < cards[mid]):
            return mid
        else:
            end -= 1
    return -1

def count(target):
    cnt = 0
    for i in range(left, n):
        if cards[i] == target:
            cnt += 1
        else:
            break
    return cnt

dic = {}
for t in targets:
    # 이미 카운트했던 카드인 경우
    if dic.get(t, 0):
        result.append(dic[t])
        continue

    left = findLeftIdx(t)
    # 원소를 발견하지 못한 경우
    if left == -1:
        result.append(0)
        dic[t] = 0
        continue
    else:
        c = count(t)
        result.append(c)
        dic[t] = c
print(*result)