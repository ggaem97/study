import bisect
import sys
sys.stdin = open('10816.txt', 'r')

n = int(input())
cards = sorted(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))


def count(arr, target):
    a = bisect.bisect_left(arr, target)
    b = bisect.bisect_right(arr, target)
    return b-a

dic = dict()
result = []
for t in targets:
    # 이미 카드의 개수를 세어본 경우
    if dic.get(t, 0):
        result.append(dic[t])
        continue
    cnt = count(cards, t)
    dic[t] = cnt
    result.append(cnt)
print(*result)