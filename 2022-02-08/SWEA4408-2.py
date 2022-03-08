import sys
sys.stdin = open('4408.txt', 'r')

for tc in range(1, int(input()) + 1):
    time = 1
    n = int(input())
    route = []
    for _ in range(n):
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a
        a, b = (a+1)//2, (b+1)//2
        route.append((a,b))
    passed = [0]*201
    for start, end in route:
        # start = (start+1) // 2
        # end = (end+1) // 2
        for i in range(start, end+1):
            passed[i] += 1
    time = max(passed)

    print(f'#{tc} {time}')
