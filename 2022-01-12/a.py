def solution(N, stages):
    stages.sort()
    # print(stages)
    failLst = []
    # 1부터 n까지의 스테이지에 대한 실패율 구하기
    for i in range(1, N+1):
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
    result = []
    for data in failLst:
        result.append(data[1])

    return result



def solution(N, stages):
    answer = []
    stages.sort()
    for i in range(1, N+1):
        count = 0
        numOfPlayers = 0
        while stages:
            numOfPlayers = max(numOfPlayers, len(stages))
            if stages[0] == i:
                count += 1
                stages.pop(0)
            else:
                stages = stages[count:]
                print(stages)
                break
        # if numOfPlayers == 0:
        #     continue
        # answer.append((round(count/numOfPlayers,4), i))
    # answer.sort(key = lambda x:(-x[0],x[1]))
    # print(answer)
    result = []
    # for data in answer:
    #     result.append(data[1])
    return result