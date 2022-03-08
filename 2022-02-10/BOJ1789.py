import sys
sys.stdin = open('1789.txt', 'r')
n = int(input())
a = 1
while a <= n:
    n -= a
    a += 1
print(a-1)