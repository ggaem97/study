# import heapq
#
# h = []
# heapq.heappush(h, (1,9))
# heapq.heappush(h, (2,8))
# heapq.heappush(h, (3,7))
# heapq.heappush(h, (4,6))
# heapq.heappush(h, (5,5))


# while h:
#     print(heapq.heappop(h))
    # (1, 9)
    # (2, 8)
    # (3, 7)
    # (4, 6)
    # (5, 5)

# food_times = [3, 1, 2]
# h = []
# k = 5
# for i in range(1, len(food_times)+1):
#     heapq.heappush(h, (i, food_times[i-1]))
#
# for _ in range(k):
#     if h:
#         data = heapq.heappop(h)
#         number = data[0]
#         time = data[1]
#         heapq.heappush(())

from collections import deque

# deq = deque()
# deq.append((1,9))
# deq.append((2,8))
# deq.append((3,7))
# deq.append((4,6))
# deq.append((5,5))
#
# while deq:
#     print(deq.popleft())


def test():
    food_times = [3, 1, 2]
    deq = deque()
    k = 7
    for i in range(1, len(food_times)+1):
        deq.append((i, food_times[i-1]))

    for t in range(1,k+2):
        # print(t, '초')
        if deq:
            number, time = deq.popleft()
            # print(number, time)
            if t == k+1:
                # print(number)
                break
            if time-1 == 0:
                # print('after..', deq)
                continue
            deq.append((number, time-1))
            # print('after..', deq)
        else:
            print(-1)
            break

import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0
    previous = 0

    length = len(food_times)

    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now
    print(q)
    result = sorted(q, key=lambda x: x[1])
    # (k - sum_value) => 3
    # length = 2
    # 3초 후에 선택될 데이터를 return
    # 0  1
    # 2 '3'
    # [(8,1),(6,2)]
    return result[(k - sum_value) % length][1]


print(solution([8,6,4], 15))
