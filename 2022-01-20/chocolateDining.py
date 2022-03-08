# print(2**20)
# import math
# print(math.pow(2,20))

# arr = []
# k = 85555
# for i in range(0, 21):
#     power = 2**i
#     arr.append(power)
# pre = 1e9
# chocolate = 0
# print(arr)
# for idx, power in enumerate(arr):
#     if abs(power - k) < pre:


# 초콜릿 먹는 개수
k = 18
# 1,2,4,8,16 .. 개수를 정하기 위한 변수
size = 1
count = 0
while size < k:
    size = size << 1

size2 = size

while k > 0:
    if k >= size:
        k -= size
    else:
        size //= 2
        count += 1

print(size2, count)