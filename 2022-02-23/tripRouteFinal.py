from collections import defaultdict


def dfs(node):
    global routes, answer
    # 딕셔너리에 값이 없으면
    if not routes[node]:
        return node
    while routes[node]:
        nextNode = routes[node].pop(0)
        answer.append(dfs(nextNode))
    # 현재 노드에서 갈 수 있는 경로가 없으면
    return node


def solutions(tickets):
    global routes, answer
    answer = []
    routes = defaultdict(list)
    for a,b in sorted(tickets):
        routes[a].append(b)
    dfs('ICN')
    answer.append('ICN')
    return answer[::-1]