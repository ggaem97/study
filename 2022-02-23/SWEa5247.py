import sys
sys.stdin = open('5247.txt', 'r')


def bfs(N, M, count):
    global s, result
    print(s)
    print(N, M)
    if N > M:
        return
    if N == M:
        result = min(result, count)
        return
    s.add(N)
    if 1 <= N + 1 <= 1000000 and N+1 not in s:
        bfs(N+1, M, count+1)
        print('y')
    if 1 <= N - 1 <= 1000000 and N-1 not in s:
        bfs(N-1, M, count+1)
        print('yt')
    if 1 <= N * 2 <= 1000000 and N*2 not in s:
        bfs(N*2, M, count+1)
        print('ysd')
    if 1 <= N - 10 <= 1000000 and N-10 not in s:
        bfs(N-10, M, count+1)
        print('545y')


for tc in range(1, int(input())+1):
    result = 1e9
    n, m = map(int, input().split())
    s = set()
    bfs(n, m, 0)
    print(f'#{tc} {result}')