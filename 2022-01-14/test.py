import sys

# n = int(sys.stdin.readline())
n = 7
# soldiers = list(map(int, sys.stdin.readline().split()))
soldiers = [15, 11, 4, 8, 5, 2, 4]
soldiers = soldiers[::-1]
print(soldiers)
dp = [0]*(n+1)
for i in range(n-1):
    value = soldiers[i]
    # print('value', value)
    count = 0
    for j in range(i+1, len(soldiers)):
        print(value, soldiers[j])
        if value <= soldiers[j]:
            count += 1
            value = soldiers[j]
    print('count', count)
    dp[i] = max(count, dp[i-1])

print(dp)