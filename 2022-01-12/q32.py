import sys
sys.stdin = open('q32','r')

n = int(input())
# a = [[7],[3,8],[8,1,0],[2,7,4,4],[4,5,2,6,5]]
a = [[] for _ in range(5)]
for _ in range(n-1):
    data = list(map(int, input().split()))
    a.append(data)
box = list(map(int, input().split()))

for k in range(n-1):
    data = a.pop()
    for i in range(n-1-k):
        box[i] = max(box[i]+data[i], box[i+1]+data[i])

print(box[0])