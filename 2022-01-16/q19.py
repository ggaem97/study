from itertools import product
print(-5//2)
# print(list(product(['+','*','-','/'], repeat=n-1)))

n = 3
lst = [3,4,5]
lst = list(map(str, lst))
# lst = input().split()
mxCnt = 0
tmp = list(map(int, input().split()))
ops = []
for i in range(len(tmp)):
    if i == 0:
        ops.append()
    ops.append()
for operators in list(product(['+', '*'], repeat=n-1)):
    print('operators', operators)
    tmp = ''
    for idx, operator in enumerate(operators):
        if int(lst[idx]) < 0 and int(lst[idx+1]) > 0:
            tmp = eval('-'+lst[idx] + operator + lst[idx + 1])
        else:
            tmp = eval(lst[idx] + operator + lst[idx+1])
    mxCnt = max(mxCnt, int(tmp))

print(mxCnt)