from collections import deque


def solution(tickets):
    n = len(tickets)
    tickets.sort(key=lambda x: x[1])
    visited = {}
    graph = {}
    for ticket in tickets:
        a, b = ticket
        if a in graph.keys():
            graph[a].append(b)
        else:
            graph[a] = [b]
            visited[a] = False

    q = deque(["ICN"])
    visited["ICN"] = True
    answer = ["ICN"]
    print(graph)
    print(visited)
    while q:
        place = q.popleft()
        print("popped place is", place)
        for dest in graph[place]:
            print('dest', dest)
            if dest not in visited.keys():
                answer.append(dest)
            elif not visited[dest]:
                visited[dest] = True
                q.append(dest)
                answer.append(dest)
                print('answer', answer)
    return answer


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))