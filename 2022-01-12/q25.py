n = 4
stages = [4,4,4,4,4]

stages.sort()
# print(stages)
failLst = []
# 1부터 n까지의 스테이지에 대한 실패율 구하기
for i in range(1, n+1):
    count = 0
    for stage in stages:
        if stage == i:
            count += 1
    failure = round(count/len(stages), 5)
    # print(failure)
    failLst.append((failure, i))
    stages = stages[count:]
# print(result)
failLst.sort(key=lambda x:-x[0])
mxCnt = []
for data in failLst:
    mxCnt.append(data[1])

print(mxCnt)