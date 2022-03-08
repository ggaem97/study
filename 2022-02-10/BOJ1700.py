from collections import defaultdict
import sys

sys.stdin = open('1700.txt', 'r')

n, k = map(int, input().split())
dic = defaultdict(int)
sequence = list(map(int, input().split()))
# 전기용품명 : 등장 횟수
for data in sequence:
    dic[data] += 1
# 전기용품명을 담음
tab = []
count = 0
for i in range(k):
    name, prior = sequence[i], dic[sequence[i]]
    # 플러그에 이미 꽂혀있는 경우
    if name in tab:
        dic[name] -= 1
        continue
    target_idx = -1
    # 플러그가 전부 차있는 경우
    if len(tab) == n:
        # 앞으로 나올 횟수 0인 name 구하기
        for idx, nm in enumerate(tab):
            if dic[nm] == 0:
                target_idx = idx
        # 앞으로 나올 횟수 0인 name 없음 > 가장 늦게 나올 name 구하기
        if target_idx == -1:
            tmp = []
            for nm in tab:
                tmp.append((nm,sequence[i + 1:].index(nm)))
            tmp.sort(key=lambda x:-x[1])
            target_idx = tab.index(tmp[0][0])
        # 꺼내기
        tab.pop(target_idx)
        count += 1
    tab.append(name)
    dic[name] -= 1
print(count)
