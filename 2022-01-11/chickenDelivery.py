from itertools import combinations
import sys

sys.stdin = open('chicken', 'r')

n, m = map(int, input().split())
chickenStore = []
house = []
# 치킨집, 집 좌표 저장
for x in range(n):
    row = list(map(int, input().split()))
    for y in range(n):
        if row[y] == 2:
            chickenStore.append((x, y))
        elif row[y] == 1:
            house.append((x, y))


# 치킨 거리 구하기
def getDistance(positions):
    distance = 0
    # house : [(0, 0), (0, 4), (1, 0), ... , (4, 0), (4, 4)]
    for hx, hy in house:
        value = 1e9
        for px, py in positions:
            dis = abs(hx - px) + abs(hy - py)
            value = min(value, dis)
        distance += value
    return distance


minVal = 1e9
for positions in list(combinations(chickenStore, m)):
    d = getDistance(positions)
    minVal = min(d, minVal)

print(minVal)
