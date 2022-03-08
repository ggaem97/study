from copy import deepcopy
import sys
from collections import defaultdict
sys.stdin = open('1700-1.txt', 'r')
n, k = map(int, input().split())
sequence = list(map(int, input().split()))
# 전기용품명을 담음
tab = []
count = 0
for i in range(k):
    name = sequence[i]
    # 플러그에 이미 꽂혀있는 경우
    if name in tab:
        continue
    # 플러그가 전부 차있는 경우
    if len(tab) == n:
        tmpTab = deepcopy(tab)
        # 앞으로 등장하지 않을 전기 용품 제거하기
        for j in range(i+1, k):
            if len(tmpTab) == 1:
                break
            if sequence[j] in tmpTab:
                tmpTab.remove(sequence[j])
        tab.remove(tmpTab[0])
        count += 1
    # 꽂기
    tab.append(name)
print(count)
