import sys
sys.stdin = open('1969.txt', 'r')

n, m = map(int, input().split())
genes = [input() for _ in range(n)]
genes.sort()
distance = [0]*n


def getHammingDistance(target):
    count = 0
    for gene in genes:
        for i in range(m):
            if target[i] != gene[i]:
                count += 1
    return count


for idx, gene in enumerate(genes):
    cnt = getHammingDistance(gene)
    distance[idx] = cnt
minDist = min(distance)
idx = distance.index(minDist)
print(genes[idx])
print(minDist)