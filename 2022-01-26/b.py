import sys
sys.stdin = open('retired', 'r')
n = int(input())
dp = [0]*(n+1)
t = [0]*n
p = [0]*n
for i in range(n):
  t[i],p[i] = map(int, input().split())

for i in range(n):
    if t[i] <= n - i:
        dp[i + t[i]] = max(dp[i] + p[i], dp[i+t[i]])
    dp[i+1] = max(dp[i+1], dp[i])

print(max(dp))

