n = int(input())
for t in range(n):
    k = int(input())
    price = list(map(int, input().split()))
    maxPrice = price[-1]
    answer = 0
    for i in range(k-2, -1, -1):
        if price[i] > maxPrice:
            maxPrice = price[i]
            continue
        answer += (maxPrice - price[i])
    print('#{} {}'.format(t + 1, answer))