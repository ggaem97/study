import sys
sys.stdin = open('2805.txt', 'r')

# 나무의 수, 가져오려고 하는 나무 길이
n, m = map(int, input().split())
height = list(map(int, input().split()))
result = 0


def findMaxHeight(arr, start, end):
    global result

    if start > end:
        return
    while start <= end:
        mid = (start + end)//2
        total = 0
        for h in height:
            if h > mid:
                total += h - mid
        # 가져오려는 나무 길이(m)보다 길거나 같다면
        if total >= m:
            # 절단 높이를 키워야
            start = mid + 1
            result = max(result, mid)
        # 가져오려는 나무 길이(m)보다 짧다면
        else:
            # 절단 높이를 줄여야
            end = mid - 1


findMaxHeight(height, 0, max(height))
print(result)
# print(findMaxHeight(height, 0, n-1))