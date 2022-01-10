n = 7
target = 4
numbers = [1,1,2,2,2,2,3]

start = 0
last = len(numbers)-1

def findFistOne(start, last):
    if start > last:
        return None
    while start <= last:
        mid = (start+last)//2
        if numbers[mid] == target and (numbers[mid-1]<numbers[mid] or mid == 0):
            return mid
        elif numbers[mid] >= target:
            last = mid - 1
        else:
            start = mid + 1

    return -1

def findLastOne(start, last):
    if start > last:
        return None

    while start<=last:
        mid = (start + last) // 2
        if numbers[mid] == target and (numbers[mid + 1] > numbers[mid] or mid == n-1):
            return mid
        elif numbers[mid] <= target:
            start = mid + 1
        else:
            last = mid - 1
    return -1

res = findLastOne(start,last)-findLastOne(start,last)
if res != 0:
    print(res)
else:
    print(-1)