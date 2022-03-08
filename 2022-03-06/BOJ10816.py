import sys
sys.stdin = open('10816.txt', 'r')

n = int(input())
cards = sorted((map(int, input().split())))
m = int(input())
targets = list(map(int, input().split()))
result = []
def findLeftIdx(target):
    global left
    start, end = 0, n-1
    while start <= end:
        mid = (start + end)//2
        if cards[mid] < target:
            start = mid + 1
        elif cards[mid] > target:
            end = mid - 1
        elif cards[mid] == target and (mid == 0 or cards[mid-1] < cards[mid]):
            left = mid
            break
        else:
            end -= 1

def findRightIdx(target):
    global right
    start, end = 0, n-1
    while start <= end:
        mid = (start + end)//2
        if cards[mid] < target:
            start = mid + 1
        elif cards[mid] > target:
            end = mid - 1
        elif cards[mid] == target and (mid == n-1 or cards[mid] < cards[mid+1]):
            right = mid
            break
        else:
            start += 1


for t in targets:
    left = -1
    findLeftIdx(t)
    if left == -1:
        result.append(0)
        continue
    else:
        right = -1
        findRightIdx(t)
        result.append(right-left+1)
print(*result)