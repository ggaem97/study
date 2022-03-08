import sys
sys.stdin = open('2437.txt', 'r')
n = int(input())
weights = list(map(int, input().split()))
# print(weights)
dp = [0]*(sum(weights)+1)


# dfs : 합쳐야하는 타겟 넘버의 개수가 2개일 때만 확인하기
# 일반화하기) 타겟 넘버의 개수가 2, .... n 일때
def dfs(count, arr, target):
    global dp
    # if dp[sum(arr)] == 1:
    #     return
    # k개가 카운팅된 경우
    if count == target:
        dp[sum(arr)] = 1
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            arr.append(weights[i])
            dfs(count+1, arr, target)
            visited[i] = False
            arr.pop()


# visited = [False]*n
# dfs(0, [])
# result = set()
# target = 3
# visited = [False] * n
# dfs(0, [])
# print(dp)

# for idx, data in enumerate(dp):
#     if data == 1:
#         result.add(idx)
# [2, 3, 4, 5, 7, 8, 9, 10, 13, 31, 32, 33, 36, 37]
# {4, 5, 6, 8, 9, 10, 11, 14, 15, 16, 32, 33, 34, 35, 37, 38, 39, 40, 43}
# print(result)

for i in range(1, n+1):
    visited = [False] * n
    target = i
    dfs(0, [], i)
    # print()
    # for idx, data in enumerate(dp):
    #     if data == 1:
    #         result.add(idx)
    # print(result)
    # print('************')
for i in range(1, sum(weights)+1):
    if dp[i] == 0:
        print(i)
        break