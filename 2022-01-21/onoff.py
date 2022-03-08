import sys
sys.stdin = open('onoff.txt', 'r')
n = int(input())
# idx 값 맞추기 위해 0번에 미지값 추가
bulbs = [-1] + list(map(int, input().split()))
k = int(input())
students = [tuple(map(int, input().split())) for _ in range(k)]

for sex, num in students:
    if sex == 1:
        # for i in range(n):
        #     if (i+1) % num == 0:
        for i in range(num, n+1, num):
            bulbs[i] = 1 - bulbs[i]
    else:
        # num -= 1
        bulbs[num] = 1 - bulbs[num]
        start, end = num-1, num+1
        while start >= 1 and end <= n:
            if bulbs[start] == bulbs[end]:
                # start -= 1
                # end += 1
                bulbs[start] = 1 - bulbs[start]
                bulbs[end] = 1 - bulbs[end]
                start -= 1
                end += 1
            else: break
        start += 1
        end -= 1
        # for i in range(start, end+1):
        #     bulbs[i] = 1 - bulbs[i]

        # bulbs[num] = 1 - bulbs[num]
        # for k in range(n//2):
        #     if num + k > n or num - k < 1: break
        #     if bulbs[num+k] == bulbs[num-k]:
        #         bulbs[num+k] = 1 - bulbs[num+k]
        #         bulbs[num-k] = 1 - bulbs[num-k]
        #     else:
        #         break

for i in range(1, n+1):
    print(bulbs[i], end=' ')
    # if i!=0 and i%20 == 0:
    if i % 20 == 0:
        print()