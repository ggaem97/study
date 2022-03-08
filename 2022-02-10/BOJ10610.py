from itertools import permutations

number = list(input())
n = len(number)
answer = [-1]

# 순열을 이용하여 숫자 배치하기
for data in permutations(number, n):
    # 맨 앞 자리수가 0이 아닌 경우
    if data[0] != '0':
        # 숫자 생성
        d = int(''.join(data))
        # 30의 배수인 경우
        if d%30 == 0:
            answer.append(d)
print(max(answer))
