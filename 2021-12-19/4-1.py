import sys
sys.stdin = open('in4.txt','r')
n = int(input())
steps = list(input().split())
# print(steps)
x = 1
y = 1
for step in steps:
    if step == 'U' and 0<x-1<=n:
        x = x-1
    if step == 'D' and 0<x+1<=n:
        x = x+1
    if step == 'R' and 0<y+1<=n:
        y = y+1
    if step == 'L' and 0<y-1<=n:
        y = y-1

print(x, y)
