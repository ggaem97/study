import sys
input = sys.stdin.readline

n, l = map(int, input().split())
pools = []
maxPool = 0
for _ in range(n):
    a, b = map(int, input().split())
    pools.append((a,b))
    maxPool = max(maxPool, b)

m = [0]*maxPool
for pool in m:
    a,b = pool
    for i in range(a,b):
        m[i] = 1
cnt = 0
for i in range(maxPool):
    if m[i] == 1:
        m[i], m[i+1], m[i+2] = 0,0,0
        cnt += 1

print(cnt)