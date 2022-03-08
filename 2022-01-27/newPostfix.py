import sys
sys.stdin = open('postfix.txt', 'r')
n = int(input())
sentence = input()
stack = []
nums = [int(input()) for _ in range(n)]
for s in sentence:
    if ord('A') <= ord(s) <= ord('Z'):
        number = nums[ord(s) - ord('A')]
        stack.append(number)
        continue
    w2 = stack.pop()
    w1 = stack.pop()
    answer = eval(str(w1) + s + str(w2))
    stack.append(answer)

print("%.2f"%stack[0])