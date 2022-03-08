import sys
sys.stdin = open('maraton.txt', 'r')
n = int(input())
pairs = [tuple(map(int, input().split())) for _ in range(n)]


def distance(a,b):
    return abs(pairs[a][0] - pairs[b][0]) + abs(pairs[a][1] - pairs[b][1])


dist=0
for i in range(0, n-1):
    dist += distance(i, i+1)

jump = 0
for i in range(1, n-1):
    jump = max(jump, distance(i-1, i) + distance(i, i+1) - distance(i-1, i+1))
print(dist-jump)