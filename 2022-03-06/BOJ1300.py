import sys
sys.stdin = open('1300.txt', 'r')

n = int(input())
k = int(input())
# n = 3이라면 1~9까지 숫자
# 숫자를 찾을때 이진 탐색 사용

def binarySearch(arr, target):
    start, end = 0, n*n-1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        # else:
        #     end


def makeNum(N):
    board = []
    for i in range(1, N+1):
        for j in range(1, N+1):
            board.append(i*j)
    return board

B = sorted(makeNum(n))
print(B)
print(B[k])
