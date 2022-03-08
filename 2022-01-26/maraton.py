import sys
sys.stdin = open('maraton.txt', 'r')
n = int(input())
pairs = [tuple(map(int, input().split())) for _ in range(n)]
maxDistance = 0
idx = 0
res = 0
# res = abs(pairs[0][0] - pairs[1][0]) + abs(pairs[0][1] - pairs[1][1])
for i in range(0, n-1):
    xx, yy = pairs[i]
    a, b = pairs[i+1]
    dist = abs(xx-a) + abs(yy-b)
    if maxDistance <= dist:
        maxDistance = dist
        idx = i
    res += dist
print(res)
res -= abs(pairs[idx-1][0]-pairs[idx][0])+abs(pairs[idx-1][1]-pairs[idx][1])
res -= abs(pairs[idx+1][0]-pairs[idx][0])+abs(pairs[idx+1][1]-pairs[idx][1])
res += abs(pairs[idx-1][0]-pairs[idx+1][0])+abs(pairs[idx+1][1]-pairs[idx-1][1])
print(res)