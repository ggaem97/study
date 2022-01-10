import sys

n, k = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

a=0
b=0
max_len = -4
for start in range(n):
    cnt=k
    if numbers[start]%2 == 0:
        l=1
        lt = start
        for j in range(start + 1, n):
            if cnt == 0:
                max_len = max(l,max_len)
                break
            if numbers[j]%2 == 0:
                rt = j
                cnt = cnt - (rt-lt-1)
                l+=1
                lt = j

print(max_len)