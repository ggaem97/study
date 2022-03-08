import sys
sys.stdin = open('test.txt', 'r')
# 노드의 개수, 간선의 개수


def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
# 부모 테이블 초기화
parent = [0] * (v+1)

# 자기 자신으로 부모 초기화
for i in range(1, v+1):
    parent[i] = i

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')
print()
# 부모 테이블 내용 출력
for i in range(1, v+1):
    print(parent[i], end=' ')

print()
a = [1,2,3]
b = reversed(a)
print(b)

aa = [1,2,3]
bb = sorted(aa)
print(bb)