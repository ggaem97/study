import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    num, K = input().split()
    K = int(K)
    n = len(num)
    now = [num]
    now = set(now)
    next = set()
    for _ in range(K):
        while now:
            t = list(now.pop())
            for i in range(n):
                for j in range(i+1, n):
                    t[i], t[j] = t[j], t[i]
                    next.add(''.join(t))
                    t[i], t[j] = t[j], t[i]
        now, next = next, now
    print(f'#{tc} {max(map(int,now))}')
    # for t in target:
    #     result = max(result, int(t))