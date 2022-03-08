import sys

sys.stdin = open('q23.txt', 'r')

n = int(input())
students = [[] for _ in range(n)]
for i in range(n):
    s = input().split()
    students[i].append(s[0])
    for j in range(1, len(s)):
        students[i].append(int(s[j]))
# print(students)

students.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))
for s in students:
    print(s[0])