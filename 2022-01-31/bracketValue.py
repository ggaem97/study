s = '(()[[]])([])'
stack = [s[0]]
s = s[1:]
value = 0
brackets = ['(', ')', '[', ']']

for bracket in s:
    # 스택이 마지막 값과 같은 값이라면 > (( [[
    if stack[-1] == bracket:
        stack.append(bracket)
        continue
    # [ 나 ( 라면
    if bracket == '[' or bracket == '(':
        stack.append(bracket)
    # () 모양이라면
    elif stack[-1] == '(' and bracket == ')':
        value = stack.pop()
        stack.append('2')
    # [] 모양이라면
    elif stack[-1] == '[' and bracket == ']':
        value = stack.pop()
        stack.append('3')
    # [ 숫자 ]
    elif not stack[-1] in brackets and stack[-2] == '[' and bracket == ']':
        value = stack.pop()
        stack.pop()
        stack.append(str(eval(value+'*'+'3')))
    # ( 숫자 )
    elif not stack[-1] in brackets and stack[-2] == '(' and bracket == ')':
        value = stack.pop()
        stack.pop()
        stack.append(str(eval(value+'*'+'2')))
    # 숫자 숫자
    elif not stack[-1] in brackets and not stack[-2] in brackets:
        val1 = stack.pop()
        val2 = stack.pop()
        stack.append(str(eval(val1+'+'+val2)))
        stack.append(bracket)
    print(stack)


for i in range(0, len(stack)-2):
    if stack[i] == '(' and not stack[i+1] in brackets and stack[i+1] == ')':
        value = stack.pop()
        stack.pop()
        stack.append(str(eval(value + '*' + '2')))
        print(stack)