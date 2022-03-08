import sys
sys.stdin = open('5207', 'r')


def binarySearch(arr, start, end, target):
    if start > end:
        return False
    while start <= end:
        mid = (start + end)//2
        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            return True
    return False


for tc in range(1, int(input())+1):
    result = 0
    n, m = map(int, input().split())
    a_lst = list(map(int, input().split()))
    b_lst = list(map(int, input().split()))
    for b in b_lst:
        if binarySearch(a_lst, 0, n-1, b):
            result += 1
    print(f'#{tc} {result}')