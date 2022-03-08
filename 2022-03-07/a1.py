from collections import Counter
import sys
sys.stdin = open('a1', 'r')
s = input()
n = int(input())
dic = Counter(s)
# print(dic)
result = 0
for _ in range(n):
    data = input()
    tmpDic = Counter(data)
    # 문자열 길이가 다른 경우 같은 문자쌍아님
    if len(data) != len(s):
        continue
    for k, v in dic.items():
        if dic[k] != tmpDic[k]:
            break
    # 모든 key 값에 대해 dic[k] == tmpDic[k]이라면
    else:
        # print(tmpDic)
        result += 1
print(result)