import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(T):
    n = int(input())
    price = list(map(int, input().split()))
    maxPrice = price[n-1]
    answer = 0
    for i in range(n-1, -1, -1):
        if price[i] > maxPrice:
            maxPrice = price[i]
            continue
        answer += (maxPrice - price[i])
    print('#{} {}'.format(t + 1, answer))