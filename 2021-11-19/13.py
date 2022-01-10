import sys

sys.stdin = open('in.txt','r')

for _ in range(5):
    cnt = 0
    n = int(sys.stdin.readline())
    while True:
        print('n>',n)
        if n>=5:
            cnt += n//5
            n=n%5
            print('5 cnt++',cnt)
            continue
        if n>=3:
            cnt += n//3
            n=n%3
            print('3 cnt++', cnt)
            continue
        if n!=0:
            print(-1)
            break
        else:
            print(cnt)
            break