arr = [8, 5, 1, 1, 11, 854, 2165, 55, 15]

print('pre', arr)
n = len(arr)

k = max(arr)
box = [0]*(k+1)
for element in arr:
    box[element] += 1

print('after count sort', end=' ')
for i in range(len(box)):
    if box[i] != 0:
        for _ in range(box[i]):
            print(i, end=' ')