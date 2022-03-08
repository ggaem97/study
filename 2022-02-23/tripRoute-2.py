from collections import defaultdict


def solution(tickets):
    tdict = defaultdict(list)
    # 딕셔너리 생성
    for start, end in sorted(tickets):  # 알파벳 순으로 방문하므로 정렬
        tdict[start].append(end)
    answer = []
    print('tdict', tdict)
    def dfs(node):
        if not tdict[node]:  # 딕셔너리에 값이 없으면
            return node
        while tdict[node]:
            next = tdict[node].pop(0)
            print('dfs', next, 'start!')
            answer.append(dfs(next))
        return node  # 현재 노드에서 갈 수 있는 경로가 없으면

    dfs("ICN")
    print('ans', answer)
    answer.append("ICN")
    return answer[::-1]

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))