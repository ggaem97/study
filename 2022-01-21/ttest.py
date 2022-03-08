import sys
sys.stdin = open('ttest.txt', 'r')

k = 18
chocolate = 1
while k > chocolate:
    chocolate = chocolate << 1

print(chocolate, end=' ')
cnt = 0
while k > 0:
    if k >= chocolate:
        k -= chocolate
    else:
        cnt += 1
        chocolate //= 2

print(cnt)

