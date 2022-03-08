from itertools import permutations
import sys
sys.stdin = open('1342.txt', 'r')

s = input()
n = len(s)
data = set(permutations(s, n))
cnt = 0
for d in data:
    check = False
    for i in range(n):
        if 0 <= i - 1 < n and d[i - 1] == d[i]:
            check = True
            break
        if 0 <= i + 1 < n and d[i + 1] == d[i]:
            check = True
            break
    if not check:
        cnt += 1
print(cnt)