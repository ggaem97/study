import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()
res = 0
for i in range(0, n):
    diff = abs(nums[i] - (i+1))
    res += diff

print(res)