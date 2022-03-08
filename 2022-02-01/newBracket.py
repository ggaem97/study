import sys
sys.stdin = open('br.txt', 'r')


def solution(s):
    n = len(s)
    result = 1
    answer = 0
    stack = []
    for i in range(n):
        if s[i] == '(':
            stack.append('(')
            result *= 2
        elif s[i] == ')':
            if not stack or stack[-1] == '[':
                return 0
            elif s[i-1] == '(':
                answer += result
            result //= 2
            stack.pop()
        elif s[i] == '[':
            result *= 3
            stack.append('[')
        else:
            if not stack or stack[-1] == '(':
                return 0
            elif s[i-1] == '[':
                answer += result
            result //= 3
            stack.pop()
    if stack:
        return 0
    return answer

# print(solution(input()))
data = list(input())
print(solution(data))