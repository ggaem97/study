from itertools import combinations
import sys
sys.stdin = open('2437.txt', 'r')


# 백트래킹 ? dfs 
def dfs(idx, arr, total):
    global n
    # 이미 방문한 경우
    if dic.get(total, 0):
        return
    dic[total] = 1

    visited[idx] = True
    total += weights[idx]
    dfs(idx+1, arr, total)
    total -= weights[idx]
    visited[idx] = False


n = int(input())
weights = list(map(int, input().split()))
dp = [0]*(sum(weights))
visited = [False]*n

for i in range(1, n):
    for data in list(combinations(weights, i)):
        dp[sum(data)-1] = 1
print(dp)
print(dp.index(0)+1)
