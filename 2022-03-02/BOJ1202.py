import sys
sys.stdin = open('1202.txt', 'r')
# 보석의 개수, 가방의 개수
n, k = map(int, input().split())
jewel = []
for _ in range(n):
    # 보석의 무게, 보석의 가격
    m, v = map(int, input().split())
    jewel.append((m,v))
# 가방에 담을 수 있는 최대 무게
c = [int(input()) for _ in range(k)]
# print(jewel)
# print(c)
c.sort()
jewel.sort(key=lambda x:(-x[1],x[0]))
# print(jewel)
# print(c)
result = 0
# 가방에 담을 수 있는 보석을 찾아보자
for i in range(k):
    # 더이상 보석이 없다면
    if not jewel:
        break
    for j in range(len(jewel)):
        m, v = jewel[j]
    # 보석의 무게가 가방에 담을 수 있다면
        if m <= c[i]:
            result += v
            jewel.pop(j)
            break
print(result)
