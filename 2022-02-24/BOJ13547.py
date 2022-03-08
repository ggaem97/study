import sys
sys.stdin = open('13547.txt', 'r')
for tc in range(1, int(input())+1):
    result = 'YES'
    s = input()
    print(s)
    cnt = s.count('x')
    print(cnt)
    if cnt >= 8:
        result = 'NO'
    print(f'#{tc} {result}')