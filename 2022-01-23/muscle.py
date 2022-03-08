from itertools import permutations
import sys
sys.stdin = open('muscleDecrease.txt', 'r')
n, k = map(int, input().split())
weight = list(map(int, input().split()))
res = 0
for numSeq in list(permutations(range(n), n)):
    power = 500
    res += 1
    for idx in numSeq:
        power += (weight[idx]-k)
        if power < 500:
            res -= 1
            break
print(res)