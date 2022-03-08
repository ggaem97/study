s = '()()()'
# print(list(s))
stack = []
answer = 0
tmp = 1
n = len(s)
for i in range(n):
    if s[i] == '(':
        stack.append(s[i])
        tmp *= 2
    elif s[i] == '[':
        stack.append([s[i]])
        tmp *= 3
    # ')' 라면
    elif s[i] == ')':
        # )) () [) ]) 중에서 [)이면 실패
        if not stack or stack[-1] == '[':
            answer = 0
            break
        # 이전 값이 '('인지 확인 ()
        if s[i-1] == '(':
            answer += tmp
        # )) () ])
        stack.pop()
        tmp //= 2
    # ']'라면
    else:
        # )] (] [] ]] 중에서 (]이면 실패
        if not stack or stack[-1] == '(':
            answer = 0
            break
        # 이전 값이 '['인지 확인
        if s[i - 1] == '[':
            answer += tmp
        # )] [] ]]
        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(answer)