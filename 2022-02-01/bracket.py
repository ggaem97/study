import sys
sys.stdin = open('br.txt', 'r')

# 반례 : [[()]]()]]
# why? stack을 사용하지 않으면
# 짝이 없는 마지막-1, 마지막 번째의 ']' 에 대한 문제 인식 불가능
def solution(s):
    n = len(s)
    result = 1
    answer = 0
    for i in range(n):
        if s[i] == '(':
            result *= 2
        elif s[i] == ')':
            if s[i-1] == '[':
                return 0
            elif s[i-1] == '(':
                answer += result
            result //= 2
        elif s[i] == '[':
            result *= 3
        else:
            if s[i-1] == '(':
                return 0
            elif s[i-1] == '[':
                answer += result
            result //= 3

    return answer

# print(solution(input()))
data = list(input())
print(solution(data))