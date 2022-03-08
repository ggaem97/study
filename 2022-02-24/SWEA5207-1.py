import sys
sys.stdin = open('5207', 'r')


def binarySearch(arr, start, end, target):
    check = 0
    if start > end:
        return False
    while start <= end:
        mid = (start + end)//2
        if arr[mid] < target:
            if check == 1:
                return False
            start = mid + 1
            check = 1
        elif arr[mid] > target:
            if check == -1:
                return False
            end = mid - 1
            check = -1
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