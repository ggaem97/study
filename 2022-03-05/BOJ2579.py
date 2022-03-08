import sys
sys.stdin = open('2579.txt', 'r')
n = int(input())
stairs = [int(input()) for _ in range(n)]
# dp[x] : x 번째까지 이동했을 때의 최대 점수
dp = [0]*(n+1)


def dynamic():
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    for i in range(2, n):
        # i-2번째에서 i번째 계단을 밟는 경우
        dp[i] = max(dp[i], dp[i-2] + stairs[i])
        # i-1번째에서 i번째 계단을 밟는 경우
        dp[i] = max(dp[i], dp[i-3]+stairs[i-1]+stairs[i])


if n == 1:
    print(stairs[0])
elif n == 2:
    print(stairs[0] + stairs[1])
else:
    dynamic()
    print(dp[n-1])