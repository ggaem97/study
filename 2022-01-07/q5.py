import sys
# sys.stdin = open('in5-1.txt', 'r')
sys.stdin = open('in5-2.txt', 'r')

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
cnt = 0
for i in range(n-1):
    for j in range(i+1, n):
        if numbers[i] != numbers[j]:
            cnt += 1

print(cnt)
