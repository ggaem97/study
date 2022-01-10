import datetime
# print(datetime.datetime.now())
# 2021-12-15 15:43:30.530253

n,m = 4,6
arr = [19,15,10,17]

arr.sort()
first = 0
last = arr[-1]
res = 0
while first <= last:
    riceLen = 0
    mid = (first+last)//2
    print('mid>',mid)
    for data in arr:
        if data > mid:
            riceLen += (data-mid)
    print('riceLen',riceLen)
    if riceLen < m:
        last = mid-1
    else:
       res = mid
       first = mid+1

print(res)
# print(datetime.datetime.now())
# 2021-12-15 15:59:48.278618