import sys
sys.stdin = open('4408.txt', 'r')

for tc in range(1, int(input()) + 1):
    time = 1
    n = int(input())
    # route = [tuple(map(int, input().split())) for _ in range(n)]
    route = []
    for _ in range(n):
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a
        a, b = (a+1)//2, (b+1)//2
        route.append((a, b))
    for i in range(n):
        start, dst = route[i]
        for target in range(start, dst+1):
            cnt = 0
            for j in range(n):
                next_start, next_dst = route[j]
                if next_start <= target <= next_dst:
                    cnt += 1
            time = max(time, cnt)

    print(f'#{tc} {time}')
