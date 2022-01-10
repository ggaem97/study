import sys

cnt = 0
n = int(sys.stdin.readline())

while True:
    if n%5 == 0:
        cnt += n//5
        break
    else:
        n-=3
        cnt+=1
    if n<0:
        print(-1)
        break
if n>=0:
    print(cnt)