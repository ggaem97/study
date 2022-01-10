n = 7
target = 4
numbers = [1,1,2,2,2,2,3]

start = 0
last = len(numbers)-1

def findOne(start, last):
    cnt = 0
    a = 1
    b = -1
    while start <= last:
        mid = (start+last)//2

        if numbers[mid] < target:
            start = mid+1
        elif numbers[mid] > target:
            last = mid-1
        else:
            cnt = 1
            while (mid + a)<n:
                if numbers[mid+a] == numbers[mid]:
                    cnt += 1
                a+=1
            while 0<=(mid + b):
                if numbers[mid+b] == numbers[mid]:
                    cnt +=1
                b-=1
            return cnt
    return -1


print(findOne(start,last))
