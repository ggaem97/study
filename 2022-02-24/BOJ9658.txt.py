import sys
sys.stdin = open('9658.txt', 'r')
for tc in range(1, int(input())+1):
    n = input()
    k = (len(n)-1)
    n = round(int(n)*(0.1)**k,1)
    if n == 10:
        k += 1
        n *= 0.1
    answer = str(n)+'*10^'+str(k)
    print(f'#{tc} {answer}')