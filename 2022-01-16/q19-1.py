n = 3
numbers = [3,4,5]
operators = [1,0,1,0]
add, sub, mul, div = operators
# x = ['+','-','*','/']
max_val = -1e9
min_val = 1e9


def DFS(i, now):
    global max_val, min_val
    global add, sub, mul, div
    print('i',i)
    if i == n:
        max_val = max(max_val, now)
        min_val = min(min_val, now)

    else:
        print(add, sub, mul, div)
        if add > 0:
            print('!')
            add -= 1
            DFS(i+1, now+numbers[i])
            add += 1
        if sub > 0:
            print('!!...')
            sub -= 1
            DFS(i+1, now-numbers[i])
            sub += 1
        if mul > 0:
            print('!!')
            mul -= 1
            DFS(i+1, now*numbers[i])
            mul += 1
        if div > 0:
            print('!!!')
            div -= 1
            DFS(i+1, int(now/numbers[i]))
            div += 1


DFS(1, numbers[0])
print(min_val)
print(max_val)