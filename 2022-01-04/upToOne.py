n = 17
k = 4
box = [1e9]*(n+1)
box[n] = 0
print(box)

for i in range(n-1, 0, -1):
    if (i%k == 0 or i == 1) and i*k <= n:
        box[i] = min(box[i*k]+1, box[i+1]+1)
    else:
        box[i] = box[i+1]+1

print(box)