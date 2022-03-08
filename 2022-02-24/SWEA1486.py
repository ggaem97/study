import sys
sys.stdin = open('5207', 'r')


# B 이상인 height 중에서 가장 작은 height 구하기
def dfs(N, B, height):
    global result, stack
    # 높이가 B 이상이라면
    if height >= B:
        result = min(result, height)
        return
    # 높이가 B 이하라면
    while stack:
        # 만약 방문하지 않았다면
        if not visited[i]:
        # dfs 처리 (스택으로 구현)
            dfs(N, B, height+employees[i])
            visited[i] = True


for tc in range(1, int(input())+1):
    result = 1e9
    n, b = map(int, input().split())
    # 직원들의 키
    employees = list(map(int, input().split()))
    # 방문처리
    visited = [False for _ in range(n + 1)]
    stack = []
    dfs(n, b, 0)
    print(f'#{tc} {result-b}')