# from itertools import combinations
#
# n = 5
# c = 3
# nums = [1,2,4,8,9]
# 컴비네이션을 이용한 풀이
# comb = list(combinations(nums, 3))
# mx = 0
# for lst in comb:
#     a = lst[1] - lst[0]
#     b = lst[2] - lst[1]
#     m = min(a,b)
#     mx = max(m, mx)
#
# print(mx)

# 이진탐색을 이용한 풀이
n = 5
c = 3
nums = [1,2,4,8,9]
start = nums[0]
last = nums[-1]-nums[0]
res=0
# gap 구하기
while start<=last:
    # print('start',start,' last',last)
    mid = (start+last)//2
    value = nums[0]
    cnt = 1
    for i in range(1,n):
        if nums[i]>=value+mid:
            # print('num',nums[i],'value',value)
            value = nums[i]
            cnt += 1
    print('cnt>',cnt)

    if cnt >= c:
        res = mid
        start = mid+1
    else:
        last=mid-1

print(res)

