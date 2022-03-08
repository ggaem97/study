def solution(s):
    n = len(s)
    result = 1
    answer = 0
    # stack 생성
    stack = []
    for i in range(n):
        if s[i] == '(':
            stack.append('(')
            result *= 2
        elif s[i] == ')':
            # s[i-1] -> stack[-1]로 구현
            # 위치를 바꾸어 구현하면 indexError 발생 ☆
            # if (stack[-1] == '[' and stack) or not stack:
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

data = input()
print(solution(data))