import sys
import bisect
sys.stdin = open('a27', 'r')

def countValue(arr, leftValue, rightValue):
    left_idx = bisect.bisect_left(arr, leftValue)
    right_idx = bisect.bisect_right(arr, rightValue)

    return right_idx - left_idx


n, x = map(int, input().split())
array = list(map(int, input().split()))

count = countValue(array, x,x)

if count == 0:
    print(-1)
else:
    print(count)