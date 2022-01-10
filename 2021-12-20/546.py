def solution(genres, plays):
    print(genres)
    print(plays)
    answer = []
    dic = {}
    sumDic = {}
    n = len(genres)
    for i in range(n):
        genre = genres[i]
        if genre in dic.keys():
            dic[genre][i] = plays[i]
            sumDic[genre] += plays[i]
        else:
            dic[genre] = {i: plays[i]}
            sumDic[genre] = plays[i]
    dic = dict(sorted(dic.items(), key=lambda x:(-sum(x[1].values()))))
    for k, valueDic in dic.items():
        valueDic = dict(sorted(valueDic.items(), key=lambda x:-x[1]))
        dic[k] = valueDic
    print(dic)

    for valueDic in dic.values():
        i = 0
        for k in valueDic.keys():
            answer.append(k)
            i += 1
            if i == 2:
                break

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"],
               [500, 600, 150, 800, 2500]))