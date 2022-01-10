from itertools import product
import sys
sys.stdin = open('in.txt','r')
n = int(input())
num = list(map(int, input().split()))
operation = []
tmp = list(map(int, input().split()))
for i in range(4):
    if tmp[i]!=0 and i==0:
        for _ in range(tmp[i]):
            operation.append('+')
    if tmp[i]!=0 and i==1:
        for _ in range(tmp[i]):
            operation.append('-')
    if tmp[i]!=0 and i==2:
        for _ in range(tmp[i]):
            operation.append('*')
    if tmp[i]!=0 and i==3:
        for _ in range(tmp[i]):
            operation.append('//')

print(operation)
largest=0
smallest=15646584887
def factorial(num):
    total = 1
    for n in range(1,num+1):
        total *= n
    return num
def calculate():
    global largest
    global smallest
    for op in list(product(operation,repeat=(n-1))):
        print(op)
        cpy = num[:]
        sum = cpy.pop(0)
        for i in range(n-1):
            sum = eval(str(sum)+op[i]+str(cpy.pop(0)))
        print(sum)
        largest = max(sum, largest)
        smallest = min(sum, smallest)

calculate()
print(largest)
print(smallest)