import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    h = []
    for i in range(k):
        heapq.heappush(h, (food_times[i], k+1))

    sumTime = 0
    preTime = 0
    length = len(food_times)
    while sumTime + (h[0][0]-preTime)*length <= k:
        data = heapq.heappop(h)
        sumTime += data[0]*length
        length -= 1
        preTime = data[0]

    result = sorted(h, key=lambda x:x[1])
    return result[(k - sumTime)%length][0]


print(solution([8,6,4],15))
