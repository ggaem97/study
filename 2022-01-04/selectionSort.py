arr = [8,5,1,11,854,5,2165,1,55,15]
print('pre', arr)
n = len(arr)
for i in range(n):
    for j in range(i+1,n):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print('after selection sort', arr)