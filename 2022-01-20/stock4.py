import sys
sys.stdin = open('a.txt', 'r')
T = int(input())
for _ in range(T):
    n = int(input())
    nums = list(map(int, input().split()))[::-1]
    high = nums[0]
    res = 0
    for num in nums:
        if high < num:
            high = num
        res += high - num
    print(res)


