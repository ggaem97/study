import sys
sys.stdin = open('4408.txt', 'r')

for tc in range(1, int(input())+1):
    n = int(input())
    corridor = [0]*401
    for i in range(n):
        a, b = map(int, input().split())
        if a%2 != 0:
            a += 1
        if b%2 != 0:
            b += 1
        if a > b:
            a, b = b, a
        a //= 2
        b //= 2
        corridor[a:b+1] = [x+y for x, y in zip(corridor[a:b+1], [1]*((b-a)+1))]
    print(f'#{tc} {max(corridor)}')