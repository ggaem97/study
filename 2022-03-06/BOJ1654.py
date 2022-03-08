import sys
sys.stdin = open('1654.txt', 'r')

k, n = map(int, input().split())
rope = [int(input()) for _ in range(k)]


def getCount(l):
    cnt = 0
    for r in rope:
        cnt += r // l
    return cnt


def binarySearch(target):
    start, end = 1, max(rope)
    result = 0
    while start <= end:
        mid = (start+end) // 2
        count = getCount(mid)
        # 목표치보다 크거나 같다면
        if count >= target:
            # 랜선 길이를 늘려야
            start = mid + 1
            result = max(result, mid)
        # 목표 갯수보다 적다면
        else:
            # 랜선 길이를 줄여야
            end = mid - 1

    return result


print(binarySearch(n))