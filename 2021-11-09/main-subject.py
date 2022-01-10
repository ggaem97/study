import sys
sys.stdin = open('in.txt','r')
n = int(input())
studnts = [[] for _ in range(n)]
for i in range(n):
    a,b,c,d = input().split()
    studnts[i] = [a,int(b),int(c),int(d)]
# res = sorted(studnts, key=lambda x:x[1], reverse=True)
res = sorted(studnts, key=lambda x: (-x[1], x[2], -x[3], x[0]))
for i in range(n):
    print(res[i][0])