from collections import defaultdict
import sys
sys.stdin = open('1342.txt')
s = input()


def dfs(pre_word, count):
    print('pre_word, count', pre_word, count)
    print('counter', counter)
    print('count', count)
    # 만약 word의 길이가 카운트 수와 같아졌다면
    if count == len(s):
        return 1
    answer = 0
    for key in counter.keys():
        print('key', key, '시작', count)
        # 이전에 비교한 문자랑 같은 문자라면 무시
        if pre_word == key:
            continue
        # 해당 문자의 value 값이 0이라면 무시 (다 써버림)
        if counter[key] == 0:
            continue
        # 해당 문자 사용
        counter[key] -= 1
        answer += dfs(key, count+1)
        print('key',key,'일때 종료', count)
        # 사용 후 반납
        counter[key] += 1
    return answer

counter = defaultdict(int)
for w in s:
    counter[w] += 1
print(counter)
print(dfs('', 0))

