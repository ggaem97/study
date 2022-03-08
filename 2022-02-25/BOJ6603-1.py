def dfs(stack, idx):
    if len(stack) == 6:
        # print 한다
        print(*stack)
        return
    for idx in range(idx, k):
        # 원소를 추가한다
        stack.append(s[idx])
        dfs(stack, idx+1)
        stack.pop()


while True:
    s = list(map(int, input().split()))
    k = s.pop(0)
    if not s:
        break
    dfs([], 0)
    print()