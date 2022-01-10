arr = [8, 5, 1, 11, 854, 2165, 55, 15]

print('pre', arr)
n = len(arr)
for i in range(1, n):
    # if arr[i] > arr[i-1]:
    #     continue
    for j in range(i-1,-1,-1):
        if arr[j+1] < arr[j]:
            arr[j+1], arr[j] = arr[j], arr[j+1]
        else:
            break

print('after insertion sort', arr)