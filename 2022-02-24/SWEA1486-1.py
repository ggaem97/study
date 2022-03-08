import sys
sys.stdin = open('1486.txt', 'r')


# B 이상인 height 중에서 가장 작은 height 구하기
def dfs(N, B, height, idx):
    global result
    print('height, idx', height, idx)
    # 마지막 원소까지 더해버렸다면
    if idx >= N:
        # 선반의 높이 이상이고 최소값보다 작을때 갱신
        if B <= height < result:
            result = height
        return
    visited[idx] = True
    print('진입 시작...')
    dfs(N, B, employees[idx]+height, idx+1)
    print('visited', visited)
    print('*****')
    visited[idx] = False
    print('높이가 줄어든채 진입 시작...')
    dfs(N, B, height, idx+1)
    print('------idx',idx,'종료------')


T = int(input())
for tc in range(1, T+1):
    result = 1e9
    n, b = map(int, input().split())
    print('직원 수, 선반의 높이', n, b)
    # 직원들의 키
    employees = list(map(int, input().split()))
    # 방문처리
    visited = [False for _ in range(n)]
    dfs(n, b, 0, 0)
    print(f'#{tc} {result-b}')