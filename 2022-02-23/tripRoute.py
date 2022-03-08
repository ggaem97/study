from collections import deque


def dfs(start):
    global dic, visited, answer
    que = deque([start])
    answer.append(start)
    while que:
        now = que.popleft()
        if now not in dic.keys() or not dic[now]:
            break
        # 알파벳 순으로 정렬
        for nextNode in sorted(dic[now]):
            # print(nextNode)
            answer.append(nextNode)
            que.append(nextNode)
            dic[now].remove(nextNode)
            break

    pass


def solution(tickets):
    global dic, visited, answer
    answer = []
    dic = {}
    visited = {}
    for ticket in tickets:
        a, b = ticket
        if a in dic.keys():
            dic[a].append(b)
        else:
            dic[a] = [b]
            visited[a] = False
    print(dic)
    # print(visited)
    # value 오름차순 정렬
    # dic = dict(sorted(dic.items(), key=lambda x:x[1]))
    # 방문했던 곳은 다시 방문하지 않도록...
    dfs('ICN')
    print(answer)
    return answer

print(solution([["ICN", "AOO"], ["AOO", "BOO"], ["BOO", "COO"], ["COO", "DOO"], ["DOO", "EOO"], ["EOO", "DOO"], ["DOO", "COO"], ["COO", "BOO"], ["BOO", "AOO"]]) == ["ICN", "AOO", "BOO", "COO", "DOO", "EOO", "DOO", "COO", "BOO", "AOO"])
print(solution([["ICN", "AOO"], ["AOO", "BOO"], ["AOO", "COO"], ["COO", "AOO"], ["BOO", "ZOO"]]) == ["ICN", "AOO", "COO", "AOO", "BOO", "ZOO"])
print(solution([["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]) == ["ICN", "BOO", "DOO", "BOO", "ICN", "COO", "DOO", "COO", "BOO"])
print(solution([["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]) == ["ICN", "AAA", "ICN", "AAA", "ICN", "AAA"])
print(solution([["ICN", "BBB"],["ICN", "CCC"],["BBB", "CCC"],["CCC", "BBB"],["CCC", "ICN"]]) == ["ICN", "BBB", "CCC", "ICN", "CCC", "BBB"])
print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]) == ["ICN", "JFK", "HND", "IAD"])
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]) == ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"])
print(solution([["ICN", "AOO"], ["ICN", "AOO"], ["AOO", "ICN"], ["AOO", "COO"]]) == ["ICN", "AOO", "ICN", "AOO", "COO"])
print(solution([["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]) == ["ICN", "AAA", "ICN", "AAA", "ICN", "AAA"])
print(solution([["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]) == ["ICN", "BOO", "DOO", "BOO", "ICN", "COO", "DOO", "COO", "BOO"])