import sys
input = sys.stdin.readline
n, l = map(int, input().split())
pools = [list(map(int, input().split())) for _ in range(n)]
# n, l = 3 , 3
# pools = [(1,6),(8,12),(13,17)]
pools.sort(key=lambda x:x[0])
# print(pools)

cur = 0
cnt = 0
for start, end in pools:
    if start > end:
        continue
    if cur > start:
        start = cur
    while start < end:
        start += l
        cnt += 1
    cur = start

print(cnt)