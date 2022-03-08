from collections import deque
import sys
sys.stdin = open('5248.txt', 'r')


def find(parent, x):
    if parent[x] != x:
        return find(parent, parent[x])
    return x


def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    q = deque(data)
    parent = [0] + [i for i in range(1, n+1)]

    while q:
        a = q.popleft()
        b = q.popleft()
        union(parent, a, b)
    answer = set()
    for i in range(1, n+1):
        data = find(parent, i)
        answer.add(data)

    print(f'#{tc} {len(answer)}')