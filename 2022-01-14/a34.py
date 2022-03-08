import sys

n = int(sys.stdin.readline())
# n = 7
soldiers = list(map(int, sys.stdin.readline().split()))
# soldiers = [15, 11, 4, 8, 5, 2, 4]
soldiers = soldiers[::-1]
# print(soldiers)
dp = [1]*(n+1)
for i in range(1, n):
    for j in range(0, i):
        if soldiers[j] < soldiers[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))