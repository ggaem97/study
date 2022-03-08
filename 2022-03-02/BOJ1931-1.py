n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]
# 종료 시간, 종료 시간이 같다면 시작 시간순으로 정렬
time.sort(key=lambda x:(x[1], x[0]))
count = 0
end = 0
for i in range(n):
    next_start, next_end = time[i]
    if end <= next_start:
        count += 1
        end = next_end
print(count)