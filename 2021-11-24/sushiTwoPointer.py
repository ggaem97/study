import sys
from itertools import combinations
sys.stdin = open('in.txt','r')

n, d, k, c = map(int, input().split())
table = []
for _ in range(n):
    table.append(int(sys.stdin.readline()))

lp=0
rp=0

tmp = []
formed = []
for _ in range(n):
    tmp.append(table[lp])
    for rp in range(1,4):
        table[rp]
