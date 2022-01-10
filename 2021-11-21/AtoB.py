import sys
sys.stdin=open('in.txt','r')
a,b = map(int, sys.stdin.readline().split())
cnt=0
while True:
    if b%10==1:
        b=b-1
        b=b//10
        cnt+=1
    elif b%2==0:
        b//=2
        cnt+=1
    # 두 조건을 모두 만족시키지 못할 경우
    else:
        print(-1)
        break
        # print(a,b)
    if b==a:
        print(cnt+1)
        break
    if b<a:
        print(-1)
        break
