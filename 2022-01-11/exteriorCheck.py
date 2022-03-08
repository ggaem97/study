from itertools import permutations

def solution(n, weak, dist):
    answer = len(dist) + 1
    k = len(weak)
    for i in range(k):
        weak.append(weak[i]+n)
    # print(weak)
    # 시작점 선택
    for start in range(k):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[count-1] 
            for index in range(start, start+k):
                # 감당 안되는 거리면 한명 더 부름
                if weak[index] > position:
                    count += 1 
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count-1]
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer