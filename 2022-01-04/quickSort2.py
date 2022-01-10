arr = [5,7,9,0,3,1,6,2,4,8]
print('pre', arr)
n = len(arr)
def quickSort(data:list, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        if data[left] > data[pivot] and data[right] < data[pivot]:
            print('left:', left, 'right', right)
            data[left], data[right] = data[right], data[left]
            print(data)
        if data[left] <= data[pivot]:
            left += 1
        if data[right] >= data[pivot]:
            right -= 1
    tmp = left if data[left] < data[right] else right
    print(tmp)
    data[pivot], data[tmp] = data[tmp], data[pivot]
    print(data)
    quickSort(data, start, tmp-1)
    quickSort(data, tmp+1, end)

quickSort(arr, 0, len(arr)-1)
print('after quickSort', arr)