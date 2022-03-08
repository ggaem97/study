import sys
sys.stdin = open('test.txt', 'r')
n = 3
L = 3
ponds = sorted(tuple(map(int, input().split())) for _ in range(n))
print(ponds)
start = 0
res = 0
count = 0
for a, b in ponds:
    if start > a:
        a = start
    diff = b - a
    count = (diff + L - 1)//L
    res += count
    start = a + count*L

print(res)
res = 0
start = 0
for a,b in ponds:
    start = max(start, a)
    diff = b -start
    count = (diff + L-1)//L
    res += count
    start += count*L

print(res)
res = 0
position = 0
for sstart, end in ponds:
    if sstart > end:
        continue
    if position > sstart:
        sstart = position
    while sstart < end:
        res += 1
        sstart += L
    position = sstart

print(res)