import sys
sys.stdin = open('1149.txt', 'r')
n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]
pre_idx = -1
result = 0
for cost in costs:
    k = -1
    min_val = 1e9
    for i in range(3):
        if min_val >= cost[i] and pre_idx != i:
            min_val = cost[i]
            k = i
    result += min_val
    pre_idx = k
print(result)