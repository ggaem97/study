import sys
sys.stdin = open('shark.txt', 'r')
n,m = map(int, input().split())
# aquarium = [list(map(int, input().split())) for _ in range(n)]
sharks = []
for i in range(n):
    # 한 행씩 받아오기
    places = list(map(int, input().split()))
    for j, place in enumerate(places):
        if place == 1:
            # 상어의 위치
            sharks.append((i, j))

res = -1e9
for i in range(n):
    for j in range(m):
        minDist = 1e9
        for x, y in sharks:
            # distance = abs(i-x) + abs(j-y)
            distance = max(abs(i-x), abs(j-y))
            minDist = min(distance, minDist)
        res = max(minDist, res)

print(res)