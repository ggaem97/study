import sys
sys.stdin = open('in.txt','r')
# n = int(input())
# houses = list(map(int, input().split()))
# houses.sort()
#
# if n%2==1:
#     idx = n//2
#     print(houses[idx])
# else:
#     smallest=454654545644888878
#     for i in range(2):
#         sum=0
#         target = houses[i]
#         for house in houses:
#             if house == target:
#                 continue
#             else:
#                 sum+=abs(target-house)
#         smallest=min(sum,smallest)
#     print(smallest)



# import sys
sys.stdin = open('in.txt','r')
n = int(sys.stdin.readline())
houses = list(map(int, sys.stdin.readline().split()))
houses.sort()

print(houses[(n-1)//2])

