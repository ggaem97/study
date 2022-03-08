import sys
sys.stdin = open('concatTeam.txt', 'r')
v, e = map(int, input().split())

def findParent(parent, x):
    if parent[x] != x:
        parent[x] = findParent(parent, parent[x])
    return parent[x]

def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [i for i in range(v+1)]
for i in range(e):
    answer, a, b = map(int, input().split())

    if answer == 0:
        unionParent(parent, a, b)
    else:
        if findParent(parent, a) == findParent(parent, b):
            print('YES')
        else:
            print('NO')

for i in range(1, v+1):
    print(findParent(parent, i))

print(parent)
#  [0, 1, 2, 1, 2, 5, 1, 6]