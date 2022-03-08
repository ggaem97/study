from collections import Counter
import sys
sys.stdin = open('a2.txt', 'r')
answer = []
s = input()
for _ in range(int(input())):
    result = 0
    wordCount = Counter(s)
    data = input()
    delete = 0
    for d in data:
        # 문자열 s에 존재하는 단어라면
        if d in wordCount.keys():
            # 해당 키 d에 대한 값이 0보다 크다면 제거
            if wordCount[d] > 0:
                wordCount[d] -= 1
            # 더이상 쌍으로 만들수 없는 경우 삭제
            elif wordCount[d] == 0:
                delete += 1
        # 문자열 s에 존재하지 않는 단어라면 바꾸기(제거)
        else:
            delete += 1
    # 남아있는 value를 더한 값 = 바꿔야하는 문자열의 개수
    # for k, v in wordCount.items():
    #     result += v
    result += delete
    print(wordCount)
    print(result)
    answer.append(result)
print(*answer)

