import sys
input = sys.stdin.readline
# 문서
docu = input().strip()
# 검색하고자 하는 단어
s = input().strip()
# 단어 포함 개수 저장
count = 0
s_len = len(s)


def countWord(document, s):
    global count, s_len
    # 문서의 길이가 검색할 단어의 길이보다 길거나 같을 경우
    while len(document) >= s_len:
        # 검색할 단어의 위치 확인
        idx = document.find(s)
        if idx == -1:
            break
        # 검색한 단어가 포함되어 있을 경우
        count += 1
        tmp = document[idx+s_len:]
        document = tmp
    return count


print(countWord(docu, s))