import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 11):
    n = int(input())
    height = list(map(int, input().split()))
    answer = 0
    for i in range(2, n-2):
        depth = max(height[i-2], height[i-1], height[i+1], height[i+2])
        if height[i] > depth:
            answer += (height[i] - depth)

    print(f'#{t} {answer}')