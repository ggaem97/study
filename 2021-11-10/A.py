import sys
sys.stdin = open('in.txt','r')
n = int(sys.stdin.readline())
a = []
for i in range(n):
    a.append(sys.stdin.readline().strip())
a = list(set(a))
print(a)
a.sort(key=lambda x:(len(x),x))
for data in a:
    print(data)