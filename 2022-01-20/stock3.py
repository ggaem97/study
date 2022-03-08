import sys
sys.stdin = open('a.txt', 'r')
T = int(input())
for _ in range(T):
    n = int(input())
    nums = list(map(int, input().split()))
    count = 0
    res = 0
    for i in range(n-1):
        if nums[i] <= nums[i+1]:
            count += 1
            diff = abs(nums[i+1]-nums[i])
            res += (diff*count)
        else:
            count = 0

    print(res)


