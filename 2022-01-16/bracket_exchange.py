def balanced_idx(p):
    # 왼쪽 괄호 개수
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i


def check_proper(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1

    return True


def solution(p):
    answer = ''
    # 빈 문자열 처리 중요
    if p == '':
        return answer

    index = balanced_idx(p)
    print('balanced_idx is ', index)
    u = p[:index+1]
    v = p[index+1:]

    if check_proper(u):
        answer = u + solution(v)
    else:
        print('check_proper is', False)
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer

print(solution("))(("))