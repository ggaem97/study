import sys
n = int(sys.stdin.readline())
soldiers = list(map(int, sys.stdin.readline().split()))

dp = [0]*n
dp[n-1] = 1
# 무조건 마지막원소 선택하게 되어있어서 비합리적
value = soldiers[n-1]
for i in range(n-2,-1,-1):
    if soldiers[i] >= value:
        dp[i] = dp[i+1]+1
        value = soldiers[i]
    else:
        dp[i] = dp[i+1]

print(n - dp[0])
