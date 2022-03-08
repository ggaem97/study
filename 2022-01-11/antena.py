n = 4
distance = [5, 1, 7, 9]
answer = 0
minDistance = 1e9
distance.sort()
for i in range(n):
    target = distance[i]
    value = 0
    for d in distance:
        value += abs(d-target)
    # print(value)
    # 한번 sort 되었기 때문에 distance 값 중 가장 작은 원소가 answer에 저장됨
    if minDistance > value:
        minDistance = value
        # print('minVal', minDistance, 'value', value)
        answer = target
        # print(answer)

print(answer)