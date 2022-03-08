from collections import defaultdict
import sys
sys.stdin = open('10815.txt', 'r')
n = int(input())
dic = defaultdict(int)
result = []
data = list(map(int, input().split()))
for d in data:
    dic[d] = 1
m = int(input())
check_num = list(map(int, input().split()))
for c in check_num:
    if dic.get(c, 0):
        result.append(1)
    else:
        result.append(0)
print(*result)
