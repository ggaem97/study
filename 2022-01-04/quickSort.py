# arr = [8, 5, 1, 11, 854, 2165, 55, 15]
arr = [5,7,9,0,3,1,6,2,4,8]
print('pre', arr)
n = len(arr)
def quickSort(data:list):
    pivot = 0
    start = 1
    end = len(data)-1
    if start == end:
        return
    while start <= end:
        if data[start] > data[pivot] and data[end] < data[pivot]:
            print('start:', start, 'end', end)
            data[start], data[end] = data[end], data[start]
            print(data)
        if data[start] <= data[pivot]:
            start += 1
        if data[end] >= data[pivot]:
            end -= 1
    tmp = start if data[start] < data[end] else end
    print(tmp)
    data[pivot], data[tmp] = data[tmp], data[pivot]
    pivot = tmp
    quickSort(data[:pivot])
    quickSort(data[pivot+1:])

quickSort(arr)
print('after quickSort', arr)

