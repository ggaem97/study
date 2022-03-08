print(2**20)
import math

print(math.pow(2,20))

arr = [[] for _ in range(21)]
k = 85555
for i in range(0, 21):
    power = 2**i
    arr[len(str(power))].append(power)
pre = 1e9
chocolate = 0
for power in arr[len(str(k))]:
    abs(power-k)
    if power > k and abs(power-k) < pre:
        pre = abs(power-k)
        chocolate = power
print(arr)
print(chocolate, chocolate%k)