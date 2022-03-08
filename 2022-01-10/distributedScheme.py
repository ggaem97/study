import sys
sys.stdin = open('distributedScheme.txt', 'r')

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


v, e = map(int, input().split())
parent = [i for i in range(v+1)]
q = []
mxCnt = 0
maxCost = 0
for i in range(e):
    a, b, cost = map(int, input().split())
    q.append((cost, a, b))
# print(q)
# q.sort(key= lambda x:x[0])
q.sort()
# print(q)
# print(parent)
for i in range(e):
    cost, a, b = q.pop(0)
    if findParent(parent, a) != findParent(parent, b):
        # 어차피 정렬되어 있기 때문에 max 취할 필요 없음
        maxCost = max(maxCost, cost)
        unionParent(parent, a, b)
        mxCnt += cost

# print(parent)
print(mxCnt - maxCost)