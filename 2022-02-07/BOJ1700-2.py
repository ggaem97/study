from collections import defaultdict
import sys
sys.stdin = open('1700.txt', 'r')

n, k = map(int, input().split())
dic = defaultdict(int)
sequence = list(map(int, input().split()))
for data in sequence:
    dic[data] += 1
# (전기용품명, 우선순위)를 담음
tab = []
count = 0
for i in range(k):
    name, prior = sequence[i], dic[sequence[i]]
    if name in tab:
        continue
    if len(tab) == n:
        tab.sort(key=lambda x:dic[x])
        pointer = 0
        if i+n <= k:
            for name_data in sequence[i+1:i+n]:
                if tab[pointer] == name_data:
                    pointer += 1
                    continue
            tab.pop(pointer)
            count += 1
    tab.append(name)
print(count)