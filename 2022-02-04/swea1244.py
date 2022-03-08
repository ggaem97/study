import sys
sys.stdin = open('input.txt', 'r')
T = int(input())


def swapDesc(number):
    if n % 2 == 1:
        number[-1], number[-2] = number[-2], number[-1]
    return ''.join(number)


for t in range(1, T+1):
    num, n = map(int, input().split())
    num = list(str(num))
    answer = ''
    for _ in range(n):
        # 숫자가 내림차순인 경우
        if num == sorted(num, reverse=True):
            answer = swapDesc(num)
            break
        # 아닐 경우
        else:
            mid = len(num)//2
            small, s_idx = num[0], 0
            big, b_idx = num[-1], len(num)-1
            for i in range(mid):
                if small > num[i]:
                    small = num[i]
                    s_idx = i
            for i in range(len(num)-1, mid-1, -1):
                if big < num[i]:
                    big = num[i]
                    b_idx = i
            num[b_idx], num[s_idx] = num[s_idx], num[b_idx]
        answer = ''.join(num)

    print(f'#{t} {answer}')

