# from collections import defaultdict
import sys
sys.stdin = open('1969.txt', 'r')

n, m = map(int, input().split())
data = [input() for _ in range(n)]
data.sort()
gene = dict()
for g in data:
    gene[g] = 0
print(gene)
distance = [0]*n


def setHammingDistance(target):
    count = 0
    for g in gene:
        for i in range(m):
            if target[i] != g[i]:
                count += 1
    gene[target] = count


for idx, g in enumerate(gene):
    setHammingDistance(g)
minDist = min(gene.values())
print(gene)
print(minDist)
for k in gene.keys():
    if gene[k] == minDist:
        print(k)
        break

# print(gene[idx])
# print(minDist)