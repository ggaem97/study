import sys
sys.stdin = open('1149.txt', 'r')
n = int(input())
def findColor(pre, arr):
    min_val = 1e9
    result = []
    k = 1e9
    for i in range(3):
        if arr[i] <= min_val and i != pre:
            min_val = arr[i]
            k = i
    result.append((k, min_val))
    return result

costs = [list(map(int, input().split())) for _ in range(n)]
pre_idx = 1e9
answer = 0
for cost in costs:
    color = findColor(pre_idx, cost)
    answer += color[0][1]
    pre_idx = color[0][0]
print(answer)
