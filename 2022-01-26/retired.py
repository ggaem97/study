import sys
sys.stdin = open('retired', 'r')
n = int(input())
t = [0]*(n+1)
p = [0]*(n+1)
dp = [0]*(n+2)
for i in range(n):
    t[i+1], p[i+1] = list(map(int, input().split()))

for i in range(n, 0, -1):
    dp[i] = max(dp[i+1], dp[i])
    if (i-1) + t[i] <= n:
        # dp[i] = max(dp[i+1], dp[i+t[i]]+p[i])
        dp[i] = max(dp[i], dp[i+t[i]]+p[i])
print(dp)
print(max(dp))