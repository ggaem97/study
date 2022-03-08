import sys

sys.stdin = open('서로소', 'r')

def unionParent(a, b, parent):
    a = findParent(a, parent)
    b = findParent(b, parent)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    print('..', parent)

def findParent(x, parent):
    if x != parent[x]:
        return findParent(parent[x], parent)
    return x

v, e = map(int, input().split())
parent = [i for i in range(v+1)]
print(parent)
for i in range(e):
    a, b = map(int, input().split())
    unionParent(a, b, parent)

print('각 원소가 속한 집합', end=' ')
for i in range(1, v+1):
    print(findParent(i, parent), end=' ')
print()
print('부모 테이블:', parent)
