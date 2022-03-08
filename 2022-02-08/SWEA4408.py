import sys

sys.stdin = open('4408.txt', 'r')

for tc in range(1, int(input()) + 1):
    time = 1
    n = int(input())
    # route = [tuple(map(int, input().split())) for _ in range(n)]
    route = []
    for _ in range(n):
        a,b = map(int, input().split())
        if a > b:
            a, b = b, a
        route.append((a,b))
    for i in range(n):
        start, dest = route[i]
        cnt = 1
        for j in range(i+1, n):
            if start < route[j][0] < dest or start < route[j][1] < dest:
                cnt += 1
            if start == route[j][0] and dest == route[j][1]:
                cnt += 1
        time = max(time, cnt)

    print(f'#{tc} {time}')
