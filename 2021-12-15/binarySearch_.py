import datetime
# print(datetime.datetime.now())
# 2021-12-15 15:12:18.023355
n = 5
numbers = [8,3,7,9,2,11,45,111,45,88,1,125,61,888,25,99]
m = 3
targets = [5,7,9,88,89,887]
res = []
numbers.sort()
print(numbers)
for target in targets:
    check = 'no'
    first = 0
    last = len(numbers) - 1
    # print('target',target)
    while first <= last:
        mid = (first+last)//2
        # print('mid',mid)
        if target == numbers[mid]:
            check = 'yes'
            break
        elif target < numbers[mid]:
            last = mid-1
        else:
            first = mid+1

    res.append(check)

print(res)
# print(datetime.datetime.now())
# 2021-12-15 15:22:53.256103