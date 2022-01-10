import sys

sys.stdin = open('in.txt', 'r')

n, k = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
print(nums)
lt = 0
rt = 0
res = -45454454
while lt < n:
    cnt = k
    maxLen = 1
    if nums[lt]%2 == 0:
        print('%dth target->'%(lt),nums[lt])
        source= lt
        for rt in range(lt+1, n):
            if nums[rt]%2 == 0 and (rt-source-1) <= cnt:
                print('%dth even nums ->'%(rt), nums[rt])
                cnt = cnt-(rt-source-1)
                print('cnt ->',cnt)
                maxLen += 1
                source = rt
            if cnt == 0:
                res = max(maxLen, res)
                break
    lt += 1
print(res)