import sys
sys.stdin = open('9095.txt', 'r')

dp = [0]*12
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
# dp[x] : x를 1,2,3의 합으로 나타낼 수 있는 가지 수
for _ in range(int(input())):
    data = int(input())
    print(dp[data])