import sys
sys.stdin = open('q33.txt','r')

n = int(input())
p = []
t = []
dp = [0]*(n+1)
maxVal = 0
for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

for i in range(n-1, -1, -1):
    time = i + t[i]

    if time <= n:
        dp[i] = max(p[i]+dp[time], maxVal)
        maxVal = dp[i]
    else:
        dp[i] = maxVal

print(dp[0])