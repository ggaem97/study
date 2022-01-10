# from collections import deque
# import sys
# sys.stdin = open('in1.txt','r')
# dx = [1,0,-1,0]
# dy = [0,-1,0,1]
#
# def bfs(x,y):
#     que = deque([(x,y)])
#     while que:
#         x,y = que.popleft()
#         for i in range(4):
#             xx = x+dx[i]
#             yy = y+dy[i]
#             if xx<0 or xx>N-1 or yy<0 or yy>M-1:
#                 continue
#             if graph[xx][yy] == 0:
#                 continue
#             if graph[xx][yy] == 1:
#                 graph[xx][yy]=graph[x][y] + 1
#                 que.append((xx,yy))
#     return graph[N-1][M-1]
#
# N, M = map(int, input().split())
# graph = []
# for _ in range(N):
#     graph.append(list(map(int, input())))
#
#
# print(bfs(0,0))

# q = deque([(1,1)])
# x,y = q.popleft()
# print((x,y))

# 메모이제이션

# d = [0]*100
#
# def fibo(x):
#     if x==1 or x==2:
#         return 1
#     if d[x] != 0:
#         return d[x]
#     else:
#         d[x] = fibo(x-1)+fibo(x-2)
#         return d[x]
#
# print(fibo(5))
# print(d)

# 1로 만들기

# import sys
# d = [0]*(10**6+1)
# n = int(sys.stdin.readline().strip())
# d[1]=0
# def dynamic(x):
#     for i in range(2,x+1):
#         # d[i]=d[i-1]+1
#         if i%3==0:
#             d[i] = min(d[i - 1]+1,d[i//3]+1)
#         if i%2==0:
#             d[i] = min(d[i - 1]+1,d[i//2]+1)
#         else:
#             d[i]=d[i-1]+1
#
# if n==1:
#     print(d[1])
# else:
#     dynamic(n)
#     print(d[n])



# import sys
# d = [0]*(10**6+1)
# n = int(sys.stdin.readline().strip())
# d[1]=0
#
# for i in range(2,n+1):
#     d[i]=d[i-1]+1
#     if i%3==0:
#         d[i] = min(d[i], d[i//3]+1)
#     if i%2==0:
#         d[i] = min(d[i], d[i//2]+1)
#
# print(d[n])


# 개미 전사
# import sys
# n = int(input())
# stock = list(map(int, input().split()))
#
# d = [0]*100000
# d[0]=stock[0]
# d[1]=max(stock[1],d[0])
# # d[2]=max(stock[2]+d[0],d[1])
# for i in range(2,n):
#     d[i]=max(d[i-2]+stock[i],d[i-1])
# print(d[:5])
# print(d[n-1])

import sys
n = int(sys.stdin.readline())
d = [0]*100000

d[1]=1
d[2]=3
d[3]=d[2]*2-1
for i in range(4,n+1):
    if i//2 ==0:
        d[i]=3**(i//2)
    else:
        d[i]=d[i-1]*(i//2+1)-(i//2)
# d[4]=3*3
# d[5]=d[4]*3-2

print(d[n])