from collections import deque
T = 3
# for _ in range(T):
#     n = int(input())
#     nums = list(map(int, input().split()))
count = 0
n = 3
nums = [1, 1, 3, 1, 2]
q = deque()
q.append(nums.pop(0))
for num in nums:
    if not q:
        q.append(nums.pop(0))
        continue
    elif q and q[0] >= num:
        q.append(num)
    else:
        print('num', num)
        while q:
            data = q.popleft()
            count += abs(num - data)
            nums.pop(0)

print(count)