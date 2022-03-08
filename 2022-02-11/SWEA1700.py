import sys
import copy
sys.stdin = open('1700-1.txt', 'r')
n, k = map(int, input().split())
use = list(map(int, input().split()))
multi = []
answer = 0

for i in range(k):
    if use[i] in multi:
        continue
    if len(multi) < n:
        multi.append(use[i])
        continue
    target = copy.deepcopy(multi)
    print(target)
    for j in range(i+1, k):
        if len(target) == 1:
            break
        if use[j] in target:
            target.remove(use[j])
    multi.remove(target[0])
    multi.append(use[i])
    answer += 1

print(answer)