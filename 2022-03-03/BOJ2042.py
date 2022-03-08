import sys
sys.stdin = open('2042.txt', 'r')

n, m, k = map(int, input().split())
data = [int(input()) for _ in range(n)]
total = sum(data)
for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        data[b - 1] = c
    elif a == 2:
        print(sum(data[b-1:c]))