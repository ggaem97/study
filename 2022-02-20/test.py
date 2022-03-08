data = 	[[1, 6, 25], [2, 3, 22], [2, 4, 66], [3, 1, 41], [3, 5, 24], [4, 1, 10], [4, 6, 50], [5, 1, 24], [5, 6, 2]]
# 1,2 번째만 정렬
data[:2] = sorted(data[:2])
for d in data:
    d[:2] = sorted(d[:2])
data.sort(key=lambda x:(x[0],x[1]))
print(data)