import sys
sys.stdin = open('postfix.txt', 'r')
n=int(input())
sentence=input()
a=[int(input()) for _ in range(n)]
stack=[]
for s in sentence:
    if ord("A") <= ord(s) <= ord("Z"):
        stack.append(a[ord(s) - ord("A")])
        continue
    stack[-2]=eval(str(stack[-2]) + s + str(stack[-1]))
    stack = stack[:-1]
print("%.02f" % stack[0])