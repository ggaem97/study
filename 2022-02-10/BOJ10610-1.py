import sys
sys.stdin = open('10610.txt', 'r')

a = list(map(int, input()))
# 0을 포함하지 않거나 각 자리수의 합이 3의 배수가 아닌 경우
if 0 not in a or sum(a) % 3 != 0:
    print(-1)
# 30의 배수
else:
    # 내림차순 정렬
    a.sort(key=lambda x:-x)
    data = ''.join(list(map(str, a)))
    print(data)