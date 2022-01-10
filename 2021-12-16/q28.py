n = 5
numbers = [-15, -4, 2, 8, 9, 13, 15]
start = 0
last = n-1

def fixPoint(start, last):
    while start <= last:
        mid = (start+last)//2
        if numbers[mid] < mid:
            start = mid+1
        elif numbers[mid] > mid:
            last = mid -1
        else:
            return mid
    return -1

print(fixPoint(start, last))
