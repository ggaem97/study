import sys
sys.stdin = open('1946.txt', 'r')
for _ in range(int(input())):
    n = int(input())
    scores = [list(map(int, input().split())) for _ in range(n)]
    scores.sort(key=lambda x:x[0]) #서류 순으로 줄 세우기
    count = 0
    goodInterview = 100001 # 합격한 사람 중 면접을 제일 잘 본 사람의 등수
    for i in range(n):
        s1, s2 = scores[i]
        if s2 < goodInterview:
            goodInterview = s2
            count += 1
    print(count)
