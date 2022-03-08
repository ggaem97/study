from collections import deque
import sys
sys.stdin = open('5248.txt', 'r')


def find(parent, x):
    if parent[x] != x:
        return find(parent, parent[x])
    return x


def union(parent, x, y):
    a = find(parent, x)
    b = find(parent, y)
    if a < b:
        parent[y] = x
    else:
        parent[x] = y


for tc in range(1, int(input())+1):
    answer = 0
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    q = deque(data)
    parent = [0] + [i for i in range(1, n+1)]

    while q:
        a = q.popleft()
        b = q.popleft()
        union(parent, a, b)
    p = []
    for i in range(1, n+1):
        data = find(parent, i)
        if data not in p:
            p.append(data)
            answer += 1

    print(f'#{tc} {answer}')