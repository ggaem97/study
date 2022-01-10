import sys

a,b = map(int, sys.stdin.readline().split())
cnt=0
while True:
    if b%2==1:
        b=(b-1)//10
        cnt+=1
    if b%2==0:
        b//=2
        cnt+=1
    if b==a:
        print(cnt+1)
        break
    if b<a:
        print(-1)
        break