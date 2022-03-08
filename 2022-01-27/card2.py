from collections import deque
import sys
sys.stdin = open('card.txt', 'r')

# q = deque([i+1 for i in range(int(input()))])
# while q:
#     for i in range(2):
#         a = q.popleft()
#         if not q:
#             print(a)
#             break
#         if i == 1:
#             q.append(a)


n, m = int(input()), 1
while m < n:
    m = m<<1
print(2*n-m)
