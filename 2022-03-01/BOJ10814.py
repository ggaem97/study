import sys
sys.stdin = open('10814.txt', 'r')
n = int(input())
info = []
for _ in range(n):
    a, b = input().split()
    info.append((int(a), b))

info.sort(key=lambda x:x[0])
for i in info:
    print(f'{i[0]} {i[1]}')