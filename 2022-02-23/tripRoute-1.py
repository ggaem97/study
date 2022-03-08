from collections import defaultdict


def solution(tickets):
    # 특정 타켓의 인접 리스트를 구하는 함수
    def init_graph():
        routes = defaultdict(list)  # 리스트를 딕셔너리로 변환
        for key, value in tickets:
            routes[key].append(value)
        return routes

    # 스택을 사용한 DFS
    def dfs():
        stack = ["ICN"]
        path = []  # 가려고 하는 경로를 저장하는 변수
        while stack:
            top = stack[-1]  # 맨 마지막 값
            print('***********')
            print('top', top)
            # 특정 공항에서 출발하는 표가 없다면 또는 있지만 티켓을 다 써버린 경우
            if top not in routes.keys() or len(routes[top]) == 0:
                path.append(stack.pop())
            else:
                stack.append(routes[top].pop(0))
            print('***************')
            print('routes', routes)
            print('path', path)
            print('stack', stack)
        return path[::-1]  # 거꾸로 뒤집기

    routes = init_graph()

    for r in routes:
        routes[r].sort()  # 키 r의 값을 오름차순으로 정렬
    print(routes)
    answer = dfs()
    return answer


print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))