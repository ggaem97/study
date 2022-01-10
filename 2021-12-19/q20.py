def switch(p:str):
    answer = ''
    stack = []
    reverse = False
    for s in p:
        if stack == [] and s == ')':
            stack.append('(')
            answer += '('
            reverse = True
        elif s == '(' and reverse:
            stack.pop()
            answer += ')'
            reverse = False
        elif s == '(' and stack == ['(','(']:
            stack.pop()
            stack.pop()
            data = "()("
            answer += data
        elif s == '(':
            answer += '('
            stack.append('(')
        else:
            stack.pop()
            answer += ')'
    return answer

print(switch("(()())()"))
print(switch(")("))
print(switch("()))((()"))