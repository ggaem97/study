from collections import defaultdict

animals = [('dog', 'Ricky'), ('cat', 'Momo'), ('rabbit', 'Jimmy'), ('cat', 'Chars'), ('cat', 'Pipy')]
dic = defaultdict(list)

for animal, name in animals:
    dic[animal].append(name)

# print(dic)

def solution(genres, plays):
    answer = []
    from collections import defaultdict
    s = defaultdict(dict) # classic: [곡 인덱스]
    for g,(idx,p) in zip(genres, enumerate(plays)):
        s[g][idx] = p
    # print(s)


def solution2(genres, plays):
    answer = []
    # 장르별 고유번호:재생횟수를 담음
    dic = defaultdict(dict)
    n = len(genres)
    for i, genre in enumerate(genres):
        dic[genre][i] = plays[i]
    print('dic',dic)
    # 총 재생횟수가 많은 순으로 (k:v) 정렬
    dic = dict(sorted(dic.items(), key=lambda x:(-sum(x[1].values()))))
    print('dic ordered by total plays count', dic)
    for k, valueDic in dic.items():
        # 장르별 곡 재생 횟수를 내림차순으로 정렬
        dic[k] = dict(sorted(valueDic.items(), key=lambda x:-x[1]))
    print('dic ordered by plays count by genre', dic)
    # 장르별 상위 2곡만 추출
    for valueDic in dic.values():
        for idx, k in enumerate(valueDic.keys()):
            answer.append(k)
            if idx == 1:
                break
    print(answer)
    return answer

solution(["classic", "pop", "classic", "classic", "pop"],
               [500, 600, 150, 800, 2500])

solution2(["classic", "pop", "classic", "classic", "pop"],
               [500, 600, 150, 800, 2500])