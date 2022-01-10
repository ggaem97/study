import sys

sys.stdin = open('in.txt','r', encoding='UTF-8')

arr = []
n = int(input())
print(n)
for _ in range(n):
    tmp = input().split()
    arr.append((tmp[0],tmp[1]))
print(arr)
arr.sort(key=lambda x:int(x[1]))
print(arr)

for student in arr:
    print(student[0], end=' ')