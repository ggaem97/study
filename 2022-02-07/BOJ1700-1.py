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
    # 플러그에 이미 꽃혀있는 경우
    if name in tab:
        dic[name] -= 1
        continue
    # 플러그가 꽉찼다면
    if len(tab) == n:
        # 우선순위 순으로 정렬
        tab.sort(key=lambda x:dic[x])
        p = [dic[name] for name in tab]
        # 우선순위가 같은게 여러 개라면
        if p.count(tab[0]) >= 2:
            # 당장 sequence 뒤에 나올 값은 제외하고 pop
            pointer = 0
            for j in range(i+1, k):
                if tab[pointer] == sequence[j]:
                    pointer += 1
                    continue
                tab.pop(pointer)
                count += 1
                break
        tab.pop(0)
        count += 1
    tab.append(name)
    dic[name] -= 1
print(count)