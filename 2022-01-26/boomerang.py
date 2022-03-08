import sys
sys.stdin = open('boom.txt','r')
n, m = map(int, input().split())
tree = [[] for _ in range(n)]
for i in range(n):
    tree[i] = list(map(int, input().split()))


def findMaxStrength(n, m):
    if n < 2 or m < 2:
        return 0


findMaxStrength(n, m)