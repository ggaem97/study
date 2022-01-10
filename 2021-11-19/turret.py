import math
import sys
sys.stdin = open('in.txt','r')

n = int(sys.stdin.readline())
for i in range(1,n+1):
    x, y, r, xx, yy, R = map(int, sys.stdin.readline().strip().split())

    rPlusR = r+R
    rMinusR = max(r-R,R-r)

    d = math.dist((x,y),(xx,yy))
    print('distance',d)
    d = math.sqrt(abs(x-xx)**2+abs(y-yy)**2)
    print('distance',d)
    # 외접하는 경우
    if d == rPlusR:
        print(1)
    # 두 원이 만나지 않는 경우
    elif d > rPlusR:
        print(0)
    # 내접하는 경우
    elif d == rMinusR:
        print(1)
    # 두 점에서 만나는 경우
    elif rMinusR < d < rPlusR:
        print(2)
    # 동심원인 경우
    elif r != R and x == xx and y == yy:
        print(0)
    # 하나의 원인 경우
    elif r == R and x == xx and y == yy:
        print(-1)
    # 원이 다른 원 안에 들어와 있는 경우
    else:
        print(0)
