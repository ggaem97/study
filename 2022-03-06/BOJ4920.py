import sys
sys.stdin = open('1920.txt', 'r')
n = int(input())
arr = sorted(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

def findTarget(target):
    start, end = 0, n-1
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            return True
    return False


for t in targets:
    if findTarget(t):
        print(1)
    else:
        print(0)
