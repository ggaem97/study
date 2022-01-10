import sys

sys.stdin = open('in.txt','r')


box = [-1]*5001
box[3] = 1
box[5] = 1

n = int(sys.stdin.readline())

for i in range(6,n+1):
    if box[i-3] != -1:
        box[i] = box[i-3] + 1
    if box[i-5] != -1:
        box[i] = box[i-5] + 1

print(box[n])