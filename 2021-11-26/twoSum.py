import sys

sys.stdin = open('in.txt', 'r')
n = int(sys.stdin.readline())
numLst = list(map(int, sys.stdin.readline().split()))
target = int(sys.stdin.readline())
res = 0
# start = 0
# end = n-1
# while start < n-1:
#     for end in range(start+1, n):
#         s = numLst[start] + numLst[end]
#         if s == target:
#             res+=1
#     start+=1

check = [0]*2000001
for num in numLst:
    check[num]=1
    if (target-num)> 0 and check[target-num] == 1:
        res+=1
    if (num-target) > 0 and check[num-target] == 1:
        res+=1

print(res)