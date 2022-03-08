lst = [1,2,3,4,2,5,3,1,1,2]
start = 0
end = 0
n = len(lst)-1
cnt = 0
m = 5
interval_sum = 0
for start in range(0, n):
    while interval_sum < m and end < n:
        interval_sum += lst[end]
        end += 1
    if interval_sum == m:
        cnt += 1
    interval_sum -= lst[start]


print(cnt)