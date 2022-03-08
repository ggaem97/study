from collections import deque
import sys
sys.stdin = open('a.txt', 'r')
T = int(input())
for _ in range(T):
    n = int(input())
    nums = list(map(int, input().split()))
    count = 0
    q = deque([nums.pop(0)])

    while nums:
        num = nums.pop(0)
        if not q:
            q.append(num)
            continue
        if q[0] >= num:
            q.append(num)
        else:
            while q:
                q_data = q.popleft()
                count += abs(q_data - num)

    print(count)