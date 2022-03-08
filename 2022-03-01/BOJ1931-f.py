import sys
sys.stdin = open('1931.txt', 'r')

n = int(input())
time = [list(map(int,input().split())) for _ in range(n)]
# 최대한 빨리 끝내는 순으로 정렬
time.sort(key=lambda x:(x[1],x[0]))
cnt, end = 0, 0
for i in range(n):
    # 시작하는 시간이 이전 종료 시간과 크거나 같다면
    if time[i][0] >= end:
        # 종료 시간를 초기화
        end = time[i][1]
        cnt += 1
print(cnt)
