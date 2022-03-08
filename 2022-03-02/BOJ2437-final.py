import sys
sys.stdin = open('2437.txt', 'r')
n = int(input())
weights = list(map(int, input().split()))
weights.sort()
check = 0
for w in weights:
    if check + 1 >= w:
        check += w
    else:
        break

print(check+1)