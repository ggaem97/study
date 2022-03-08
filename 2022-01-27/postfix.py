import sys
sys.stdin = open('postfix.txt', 'r')
n = int(input())
postfix = input()
operator = ['*', '-', '+', '/']
stack = []
numbers = dict()
for i in range(n):
    number = input()
    for data in postfix:
        if data == chr(i+65):
            numbers[data] = number


for data in postfix:
    # data가 문자라면 ex A, B, C, D, ...
    if data not in operator:
        stack.append(data)
    else:
        w2 = stack.pop()
        w1 = stack.pop()
        if 'A' <= str(w2) <= 'Z':
            w2 = numbers[w2]
        if 'A' <= str(w1) <= 'Z':
            w1 = numbers[w1]
        answer = eval(str(w1) + data + str(w2))
        stack.append(answer)

print("%.2f"%stack[0])
# print("{:.2f}".format(stack[0]))
# print(f"{stack[0]:.2f}")

