import sys
sys.stdin = open('1245.txt', 'r')
for tc in range(1, int(input())+1):
    n = int(input())
    line = list(map(int, input().split()))
    print('line', line)
    X = line[:n]
    M = line[n:]
    print('X', X, 'M', M)
    answer = []
    for i in range(1, n):
        low = X[i-1]
        high = X[i]
        mid = 0
        while high - low > 1/(10**12):
            mid = (low + high) / 2
            left = right = 0
            for i in range(n):
                force = M[i] / (mid-X[i])**2
                if X[i] < mid:
                    left += force
                else:
                    right += force
            if left < right:
                high = mid
            else:
                low = mid
        answer.append(mid)
    result = ''.join('%.10f' % f for f in answer)
    print(f'{tc} {result}')