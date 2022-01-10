import sys
sys.stdin = open('in.txt','r')

for _ in range(4):
    n = int(input())
    INF=1e9
    box = [-1]*5001

    box[3] = 1
    box[5] = 1

    for i in range(6,n+1):
        if i%3 == 0:
            box[i] = box[i-3] + 1
        if i%5 == 0:
            box[i] = box[i-5] + 1
        if (i%5)%3 == 0:
            box[i] = box[5*(i//5)] + box[3*((i%5)//3)]

    print(box[n])