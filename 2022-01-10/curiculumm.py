import sys
sys.stdin = open('curiculum', 'r')
v = int(input())
cnt = 0
times = [0]*(v+1)
mxCnt = [0] * (v + 1)
for i in range(v):
    line = list(map(int, input().split()))
    cnt += 1
    data = line.pop(0)
    if data == -1:
        continue
    else:
        times[cnt] = data
        mxCnt[cnt] = data
    while line:
        data = line.pop(0)
        if data == -1:
            break
        else:
            mxCnt[cnt] += times[data]

print(times)
print(mxCnt)